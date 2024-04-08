from pymongo import MongoClient
import os

db_string = os.environ.get("mongodb_string")
conn = MongoClient(db_string)
