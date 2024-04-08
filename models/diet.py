from pydantic import BaseModel

class Disease(BaseModel):
    name: str
    description: str
    vitamins_minerals: list[str]

class Food(BaseModel):
    vitamin_mineral_name: str
    foods: list[str]