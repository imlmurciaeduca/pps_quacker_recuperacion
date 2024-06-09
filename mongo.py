from pymongo import MongoClient

# TODO: hay que ver cómo apañamos la conexión para que podamos usar variables de entorno
client = MongoClient('mongodb://127.0.0.1:27017')
db = client['quacker']
users = db['users']
quacks = db['quacks']