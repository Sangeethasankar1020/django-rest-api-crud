from pymongo import MongoClient

link=MongoClient("mongodb://localhost:27017")

db=link.api
col=db.employee
