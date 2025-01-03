#!/usr/bin/env python3

import connexion
import os 
from openapi_server import encoder
from flask_sqlalchemy import SQLAlchemy
from openapi_server.controllers.contenido_controller import import_db_controller
from openapi_server.models.contenido import import_db_cont
from openapi_server.models.episodios import import_db_ep
from openapi_server.models.temporadas import import_db_temp

from flask_cors import CORS

app = connexion.App(__name__, specification_dir='./openapi/')
CORS(app.app)
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Microservicio de Contenidos de una aplicación de tipo Netflix'},
            pythonic_params=True)

load_dotenv();
app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URI', 'postgresql://usuario:contraseña@localhost:5432/Contenidos'
)

app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#esto es para que no se caiga a las 10 requests
app.app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 30,        # Tamaño máximo de conexiones en el pool
    'pool_timeout': 30,     # Tiempo máximo de espera para obtener una conexión
    'pool_recycle': 180,   # Tiempo máximo de vida de una conexión (en segundos)
    'max_overflow': 5       # Conexiones extra que pueden crearse si se alcanza el pool_size
}

db = SQLAlchemy(app.app)

import_db_controller(db)
import_db_cont(db)
import_db_ep(db)
import_db_temp(db)

app.run(port=8080)