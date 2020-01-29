from pymongo import MongoClient


db = MongoClient('mongodb://localhost:27017/')
goals_db = db['goals']
goals_collection = goals_db['goals']
