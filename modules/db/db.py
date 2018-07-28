from flask import Flask
from flask_pymongo import PyMongo
# from mongokit import 

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/uddb"
mongo = PyMongo(app)
    

# configuration
# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 27017

# # create the little application object
# app = Flask(__name__)
# app.config.from_object(__name__)

# # connect to the database
# connection = Connection(app.config['MONGODB_HOST'],
#                         app.config['MONGODB_PORT'])