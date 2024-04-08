from fastapi import APIRouter
from models.diet import Disease, Food
from config.db import conn
from schemas.diet import dietsEntity

dietr = APIRouter()


@dietr.get("/")
async def diet_story(disease_name: str) -> dict:
    try:
        disease = conn.local2.disease.find_one({"name": disease_name})
        if disease:
            required_vitamins_minerals = disease.get("vitamins_minerals")
            sources = {}
            for vit_min in required_vitamins_minerals:
                food_sources = conn.local2.food.find_one({"vitamin_mineral_name":vit_min})
                if food_sources:
                    sources[vit_min] = food_sources.get("foods")
                else:
                    sources[vit_min] = []

            output = {
                "health_condition": disease["name"],
                "description": disease["description"],
                "vitamins_required": required_vitamins_minerals,
                "sources": sources
            }
            return output
        return {"message": "disease not found"}         
        
    except Exception as ex:
        return {"Error": f"somewhere exception happened {ex}"}
    
@dietr.post("/disease")
async def create_disease_story(disease: Disease):
    conn.local2.disease.insert_one(dict(disease))
    return dietsEntity(conn.local2.disease.find())

@dietr.post("/food")
async def create_food_story(food: Food):
    conn.local2.food.insert_one(dict(food))
    return dietsEntity(conn.local2.food.find())

#######################################################################