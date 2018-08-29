import logging
from pymongo import MongoClient
from config import DATE_FORMAT
from datetime import datetime
from bson.json_util import dumps, loads
from bson import json_util
import  simplejson as json


class MongoDatabase():

    def __init__(self):
        logging.debug("##############################################")
        logging.debug("# Creating Mongo Database Connection")
        logging.debug("##############################################")

        try:
            self.client = MongoClient("mongodb://localhost:27017/")
            self.client = self.client['scraping']
        except Exception as e:
            print(e)


    def create(self,entityInstance,databaseSession=None):
        # check if entity has collection name
        collectionName = entityInstance.collectionName
        modelData = entityInstance.getModelData()
        createTime = datetime.now().strftime(DATE_FORMAT)
        modelData['createdAt'] = createTime
        lastInsertedId = self.client[collectionName].insert_one(modelData).inserted_id

        ## if insert into data base is successfull then add mongodb id in the entity instance
        entityInstance._id = lastInsertedId
        entityInstance.createdAt = createTime

    def update(self,entityInstance,databaseSession=None):

        # check if entity has collection name
        collectionName = entityInstance.collectionName
        modelData = entityInstance.getModelData()
        updateTime = datetime.now().strftime(DATE_FORMAT)
        modelData['updatedAt'] = updateTime
        self.client[collectionName].update_one({'_id': entityInstance._id},{"$set": modelData})

        ## if insert into data base is successfull then add mongodb id in the entity instance
        entityInstance.updatedAt = updateTime


    def find(self,entityClass,whereClause,databaseSession=None):
        collectionName = entityClass.collectionName
        mongoCursor = self.client[collectionName].find(whereClause)
        data = []
        for eachData in mongoCursor:
            jsonString = dumps(eachData) 
            convert = json.loads(jsonString)
            data.append(convert)

        return data
        
            

    
 
