import constants
from utils import backend

from flask import Flask, request
from flask_restful import Resource, Api
from flask_pymongo import PyMongo, wrappers, ObjectId
import os
import json
import boto3
import httplib


"""SETUP APP"""
HOST = constants.SERVER_DEFAULTS["HOST"]
PORT = constants.SERVER_DEFAULTS["PORT"]
MONGO_URL = constants.MONGO_DEFAULTS["MONGO_URL"]
SETTINGS = {
    "host": HOST,
    "port": PORT,
    "debug": False
}

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URL


"""SETUP MONGO"""
mongo = PyMongo(app)
mongo_client = wrappers.MongoClient(MONGO_URL)
MONGO_COLLECTION = mongo_client[constants.MONGO_DEFAULTS["COLLECTION_NAME"]]


"""SETUP API"""
api = Api(app)


"""SETUP S3"""
S3_BUCKET = constants.S3_DEFAULTS["BUCKET_NAME"]
AWS_ACCESS_KEY_ID = constants.S3_DEFAULTS["ACCESS_KEY"]
AWS_SECRET_ACCESS_KEY = constants.S3_DEFAULTS["SECRET_ACCESS_KEY"]


class User(Resource):
    def __init__(self):
        x = 4

    def get(self):
        return backend.server_response(message="user get endpoint")


# utility endpoint to GET simple general information
class Receipt(Resource):
    def __init__(self):
        x = 4

    def get(self):
        return backend.server_response(message="receipt get endpoint")


# add blob upload endpoint
api.add_resource(Receipt, constants.SERVER_ENDPONTS["RECEIPT"])
api.add_resource(User, constants.SERVER_ENDPONTS["USER"])
if __name__ == "__main__":
    app.run(**SETTINGS)
