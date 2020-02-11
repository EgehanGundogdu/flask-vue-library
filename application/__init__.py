from flask import Flask
from pymongo import MongoClient
import json
from config import Config
app = Flask(__name__)


app.config.from_object(Config)

client = MongoClient(
    host=app.config['MONGO_HOST'], port=int(app.config['MONGO_PORT']))
db = client.test_database
collection = db.test_collection


from application import routes  # noqa
