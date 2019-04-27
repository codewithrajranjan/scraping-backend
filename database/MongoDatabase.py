import logging
from pymongo import MongoClient
import pymongo
from config import DATE_FORMAT
from datetime import datetime
from bson.json_util import dumps
import  simplejson as json
from bson import ObjectId
import os



class MongoDatabase():

    def __init__(self):
        logging.debug("##############################################")
        logging.debug("# Creating Mongo Database Connection")
        logging.debug("##############################################")
        print("# Creating Mongo Database Connection")

        try:
            databaseConnectionString = os.environ["DATABASE_CONNECTION_STRING"]
            self.client = MongoClient(databaseConnectionString)
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
        id = entityInstance.getId()
        updateTime = datetime.now().strftime(DATE_FORMAT)
        modelData['updatedAt'] = updateTime
        self.client[collectionName].update_one(
                {'_id': ObjectId(id)},
                {"$set": modelData}
        )

        ## if insert into data base is successfull then add mongodb id in the entity instance
        entityInstance.updatedAt = updateTime

    def delete(self,entityClass,whereClause={},databaseSession=None):
        # check if entity has collection name
        collectionName = entityClass.collectionName
        self.client[collectionName].delete_one({'_id': ObjectId(whereClause['id'])})




    def find(self,entityClass,whereClause,textMatching=False,databaseSession=None):
        collectionName = entityClass.collectionName
        if 'id' in whereClause:
            temp = whereClause.get('id')
            del whereClause['id']
            whereClause['_id']= ObjectId(temp)
        mongoCursor = self.client[collectionName].find(whereClause).sort([('createdAt', pymongo.DESCENDING)])
        data = []

        for eachData in mongoCursor:
            jsonString = dumps(eachData) 
            convert = json.loads(jsonString)
            if '_id' in convert:
                temp = convert.get('_id').get('$oid')
                convert['id'] = temp

            data.append(convert)

        return data
        
            

    
 
