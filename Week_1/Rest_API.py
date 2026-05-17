from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

url = MongoClient("mongodb+srv://Internship:glaxit987543@newcluster.vlpyfwt.mongodb.net/?appName=NewCluster")

database = url["Glaxit-Internship"]

collection = database["Week1"]


app = FastAPI()

class register(BaseModel):
    name: str
    email: str
    phone: str
    password: str

class update(BaseModel):
    name: str
    email: str
    phone: str
    password: str



@app.get('/get')
def read_data():
    return {"message": "Hello World"}
                       
@app.post('/post')
def recieve_data(data: register):
    saved = collection.insert_one(data.dict())
    print(f"Data is Saved : {saved}")



    
@app.put("/put/{id}")
def update_data(id: str,data: update ):
    collection.update_one({"_id": ObjectId(id)}, {"$set": data.dict()})
    return {"message": "Data updated Successfully"}




@app.delete('/delete/{id}')
def delete_data(id: str):
    collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Data Deleted Successfully"}
