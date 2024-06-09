from pymongo import MongoClient
from os import environ

client = MongoClient(f'mongodb://{environ.get("MONGO_IP", "localhost")}:{environ.get("MONGO_PORT", "27017")}')
db = client['quacker']
users = db['users']
quacks = db['quacks']