
from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'
#comexión a la base de datos Mongo

client = MongoClient(MONGO_URI)
#creamos la base de datos en donde se va a conectar
db = client['teststore']
#creamos la coleccion en la base de datos
collection = db['products']
#guardamos un nuevo producto
#collection.insert_one({"name": "Remera", "price": 900 })
#collection.insert_one({"name": "Pantalon", "price": 1900 })
#buscamos colección elementos remera
results = collection.find({"name" : "Remera"})

for r in results:
    print(r)
#buscamos colección elementos pantalon
results = collection.find({"price":1900})
for r in results:
    print(r)
#eliminamos los elementos remera de la coleccion
#collection.delete_many({"name": "Remera"})

#realizamos la actualizacion de pantalon
#collection.update_one({"name":"Pantalon"},{"$set": {"name":"Pantalon de Jean","price": 2500}})

#vamos a retornar el tamaño de la base de datos
numero = collection.count_documents({})
print(numero)