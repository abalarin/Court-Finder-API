import os
import json

from flask import Flask

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

with open(APP_ROOT + '/config.json') as config_file:
    config = json.load(config_file)

from courtfinderapi.objectstorage.configer import getConfig
from courtfinderapi.objectstorage.authBoto import botoClient, botoResource

configParser = getConfig(APP_ROOT + '/objectstorage/config.ini')
client = botoClient(config.get('BOTO_KEY'), config.get('BOTO_SECRET'), configParser['object_api']['base_url'], configParser['object_api']['user'])
resource = botoResource(config.get('BOTO_KEY'), config.get('BOTO_SECRET'), configParser['object_api']['base_url'], configParser['object_api']['user'])


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(config.get('DB_URI'), echo=False)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

from courtfinderapi import endpoints
