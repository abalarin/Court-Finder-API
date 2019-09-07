from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

from courtfinderapi import endpoints
