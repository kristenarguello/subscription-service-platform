import random
from datetime import datetime

import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client["cadastro_geral"]


# pelo menos 10 clientes
collection = db["clientes"]
collection.create_index([("email", pymongo.ASCENDING)], unique=True)
collection.create_index([("codigo", pymongo.ASCENDING)], unique=True)
clientes = []
people_names = [
    "James",
    "Maria",
    "Robert",
    "Sophia",
    "Michael",
    "Linda",
    "William",
    "Elizabeth",
    "David",
    "Jennifer",
]
for i in range(10):
    clientes.append(
        {
            "codigo": random.randint(10000, 99999),
            "nome": people_names[i],
            "email": f"{people_names[i].lower()}@email.com",
        }
    )
    collection.insert_one(clientes[i])

# 5 aplicativos diferentes
collection = db["aplicativos"]
collection.create_index([("codigo", pymongo.ASCENDING)], unique=True)
aplicativos = []
app_names = ["QuickQuest", "FitFleet", "MindMerge", "ChoreChampion", "TravelTrove"]
for i in range(5):
    aplicativos.append(
        {
            "codigo": random.randint(10000, 99999),
            "nome": app_names[i],
            "custo_mensal": random.uniform(10.0, 25.0),
        }
    )
    collection.insert_one(aplicativos[i])

# pelo menos 5 assinaturas diferentes
collection = db["assinaturas"]
collection.create_index([("codigo", pymongo.ASCENDING)], unique=True)
assinaturas = []
for i in range(5):
    assinaturas.append(
        {
            "codigo": random.randint(10000, 99999),
            "cod_aplicativo": aplicativos[i]["codigo"],
            "cod_cliente": clientes[i]["codigo"],
            "inicio_vigencia": datetime.now(),
            "fim_vigencia": datetime.now(),
        }
    )
    collection.insert_one(assinaturas[i])
