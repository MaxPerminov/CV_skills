from pymongo import MongoClient


def connection():
  CONNECTION_STRING = "mongodb+srv://check:1234@clusterhomework.2firvzt.mongodb.net/?retryWrites=true&w=majority"
  client =  MongoClient(CONNECTION_STRING)
  return client ["homework"] #db
