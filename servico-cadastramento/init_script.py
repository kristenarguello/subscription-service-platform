import os
import random
from datetime import datetime, timedelta

import pymongo
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

uri = os.getenv("MONGO_DB_URI")
client = pymongo.MongoClient(uri)

try:
    client.admin.command("ping")
    logger.debug("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    raise e

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
            "codigo": i + 1,
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
            "codigo": i + 1,
            "nome": app_names[i],
            "custo_mensal": random.uniform(10.0, 25.0),
        }
    )
    collection.insert_one(aplicativos[i])

# pelo menos 5 assinaturas diferentes
collection = db["assinaturas"]
collection.create_index([("codigo", pymongo.ASCENDING)], unique=True)
collection.create_index([("cod_aplicativo", pymongo.ASCENDING)], unique=False)
collection.create_index([("cod_cliente", pymongo.ASCENDING)], unique=False)

start_date = datetime.now()
end_date = datetime(2025, 12, 31)


assinaturas = []
for i in range(5):
    random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
    random_datetime = start_date + timedelta(seconds=random_seconds)
    assinaturas.append(
        {
            "codigo": i + 1,
            "cod_aplicativo": aplicativos[i]["codigo"],
            "cod_cliente": clientes[i]["codigo"],
            "inicio_vigencia": datetime.now(),
            "fim_vigencia": random_datetime,
        }
    )
    collection.insert_one(assinaturas[i])
