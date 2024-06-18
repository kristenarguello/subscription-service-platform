from pymongo import MongoClient
from datetime import datetime

client = MongoClient("localhost", 27017)

db = client["cadastro_geral"]

# pelo menos 10 clientes
collection = db["clientes"]
clientes = []
for i in range(10):
    clientes.append({"codigo": 1, "nome": "", "email": ""})
    collection.insert_one(clientes[i])

# 5 aplicativos diferentes
collection = db["aplicativos"]
aplicativos = []
for i in range(5):
    aplicativos.append({"codigo": 1, "nome": "", "custo_mensal": 0.0})
    collection.insert_one(aplicativos[i])

# pelo menos 5 assinaturas diferentes
collection = db["assinaturas"]
assinaturas = []
for i in range(5):
    assinaturas.append(
        {
            "codigo": 1,
            "cod_aplicativo": aplicativos[i]["codigo"],
            "cod_cliente": clientes[i]["codigo"],
            "inicio_vigencia": datetime.now(),
            "fim_vigencia": datetime.now(),
        }
    )
    collection.insert_one(assinaturas[i])
