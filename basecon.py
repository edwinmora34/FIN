from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()
user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')
hostname = os.getenv('MONGO_HOSTNAME')
uri = f"mongodb+srv://{user}:{password}@{hostname}/?retryWrites=true&w=majority"
def conexion():

    # Cadena de conexión descargada de Mongo
    client = MongoClient(uri, server_api=ServerApi('1'))
    db=client['Laganga']#Base de datos donde se almacenaran las busquedas
    client.admin.command('ping')
    print("Conexión Exitosa!")
    return db