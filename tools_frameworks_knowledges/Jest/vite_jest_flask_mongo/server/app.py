from flask import Flask
from flask_cors import CORS
from connection import connection


app = Flask(__name__)
CORS(app)

def get_docs():
  data = connection()
  data_collection = data["hw_collection"]
  return data_collection.find({},{ "_id": 0})

def get_doc():
  data = connection()
  data_collection = data["hw_collection"]
  return data_collection.find({"name": "Sasha"},{ "_id": 0})

@app.route("/")
def home():
  data = get_docs() 
  users = []
  for doc in data:
    users.append(doc)
  return users

@app.route("/doc")
def single_doc():
  data = get_doc()
  for i in data:
    return i


if __name__ == "__main__":
  app.run(port=4321)
