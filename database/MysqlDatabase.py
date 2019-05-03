import logging
from config import DATE_FORMAT
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

class MysqlDatabase():

    def __init__(self,connectionDict):
        logging.debug("##############################################")
        logging.debug("# Creating Mysql Database Connection")
        logging.debug("##############################################")
        try:

            self.client = create_engine("mysql+pymysql://root:password@localhost/rating?charset=utf8mb4",pool_size=10)

        except Exception as e:

            print(e)

    def getSession(self):
        self.session = sessionmaker(bind=self.client)
        return self.session()
        


    def create(self,entityInstance,databaseSession=None):

        # check if entity has collection name
        collectionName = entityInstance.collectionName
        modelData = entityInstance.getModelData()
        createTime = datetime.now().strftime(DATE_FORMAT)
        modelData['createdAt'] = createTime

        keys = "("
        values = "("
        totalItems = len(modelData)
        count = 1
        for eachKey in modelData : 
            separator = ""
            if(count<totalItems):
                separator = ","
            keys += " `{}`{}".format(eachKey,separator)
            values += " '{}'{}".format(modelData[eachKey],separator)
            count = count + 1
        
        keys +=" )"
        values +=" )"

        # creating the sql query to create
        sql = "INSERT INTO `{}` {} VALUES {}".format(collectionName,keys,values)
        response = None

        if databaseSession == None :
            response = self.client.execute(sql)
        else :
            response = databaseSession.execute(sql)
         
         

        ## if insert into data base is successfull then add mongodb id in the entity instance
        entityInstance.id = response.lastrowid
        entityInstance.createdAt = createTime

    def update(self,entityInstance):

        # check if entity has collection name
        collectionName = entityInstance.collectionName
        modelData = entityInstance.getModelData()
        updateTime = datetime.now().strftime(DATE_FORMAT)
        modelData['updatedAt'] = updateTime
        self.client[collectionName].update_one({'_id': entityInstance._id},{"$set": modelData})
        
           

             
        ## if insert into data base is successfull then add mongodb id in the entity instance
        entityInstance.updatedAt = updateTime


    def find(self,entityClass,whereClause):

        tableName = entityClass.collectionName

        # creating the sql query
        sql = "SELECT * from `{}`".format(tableName)

        if len(whereClause) > 0:
            sql += " where "

            #making the string where clause string and the tuple value
            values = list()

            totalWhereClausesItems = len(whereClause) # this is calcualted so that we can attach [and] in our where clause
            count = 1
            for eachKey in whereClause: 
                 
                sql += " `{}`=%s ".format(eachKey)  # for example this will make a key as `tenantId`=%s
                
                # taking decison if we need to add where clause in the query
                if totalWhereClausesItems > count:
                    sql +=" and "

                count = count + 1
                values.append(whereClause[eachKey])
            
            data = self.client.execute(sql,values)
        else :  
            data = self.client.execute(sql)

        return data
        

    def rawQuery(self,sqlQuery,values,databaseSession=None):
        if databaseSession == None :
            data = self.client.execute(text(sqlQuery),values)
        else : 
            data = databaseSession.execute(text(sqlQuery),values)

        return data.fetchall()





