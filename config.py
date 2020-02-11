from dotenv import load_dotenv
from os.path import join, dirname
import os.path

dotenv = load_dotenv(join(dirname(__file__), '.env'))
class Config:
    MONGO_HOST = os.environ.get('MONGO_HOST')
    MONGO_PORT = os.environ.get('MONGO_PORT')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very very secret key'
