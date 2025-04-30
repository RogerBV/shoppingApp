from entities import base_metada
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entities.common import DATABASE_URI
from entities import Category
from entities import Product
import psycopg2

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

base_metada.create_all(engine)