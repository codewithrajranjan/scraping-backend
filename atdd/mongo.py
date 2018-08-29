import logging
from robot.api import logger
from pymongo import MongoClient

class MongoDB:
    
    def __init__(self,connectionString,databaseName):
        """
        Establish connection with mongodb

        Arguments
        ------------------------
        connectionString : str
            Connection string to mongodb. eg localhost:27017
        databaseName: str
            Name of the database to which connection should be made
        """
        connectionString = "mongodb://"+connectionString+"/"
        #self.client = MongoClient("mongodb://localhost:27017/")
        self.client = MongoClient(connectionString)
        self.db = self.client[databaseName]
    
    def deleteDatabase(self,databaseName):
        self.client.drop_database('billing')
        


