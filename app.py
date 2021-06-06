
from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'
#comexión a la base de datos Mongo

client = MongoClient(MONGO_URI)
#creamos la base de datos en donde se va a conectar
db = client['teststore']
#creamos la coleccion en la base de datos
collection = db['products']
#guardamos un nuevo producto
collection.insert_one({"name": "Remera", "price": 900 })