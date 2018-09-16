from .MongoDatabase import MongoDatabase
from .MysqlDatabase import MysqlDatabase
import pymysql.cursors
from config import DATABASE_LIST
connectionPool = {}

class DatabaseManager(object):
    """
    Class to manage interations with database


    Methods
    ----------------------------
    create(entityInstance,billing="billing")
        Create entityInstance in database
    find(entityClass,factoryClass,whereClause,database="billing",responseFormat="object")
        Find entity from database based on where clause
    udpate(entityInstance,database="billing")
        Upate entity in the database
    """

    connectionPool = connectionPool

    @classmethod 
    def __getDatabaseConnection(cls,entityInstanceOrClass):
        # first we need to find which database connection we need to find in the connection pool 
        # first checkin if the entityInstanceOrClass has database name or not 
        # if it doesn't contain the database name then we need to get the default database name
        databaseToFind = None
        

        if hasattr(entityInstanceOrClass,'database') == True:
            databaseToFind = entityInstanceOrClass.database
        else : 
            databaseToFind = DATABASE_LIST['defaultDatabase']

        # check if database connection is present in connection pool or not
        # if it is present then return it
        if databaseToFind in cls.connectionPool:
            return cls.connectionPool[databaseToFind]

        
        # find database config from database list config
        databaseConfig = DATABASE_LIST[databaseToFind]

        adapter = databaseConfig['adapter']
        
        connection = None
        
        # creating suitable connection based on adapter present in the config
        if adapter == "mongodb":
            # if connection doesn't exist then create a connection
            connection = MongoDatabase()

        if adapter == "mysql":
            # if connection doesn't exist then create the connection
            mysqlConfig = cls.createMySQLConnectionDict(databaseConfig)
            connection = MysqlDatabase(mysqlConfig)

        # save the connection state in connection pool 
        cls.connectionPool[databaseToFind] = connection

        # return connection
        return cls.connectionPool[databaseToFind]


    @classmethod
    def getSession(cls,databaseName):
        #find find that the database supports session or not
        databaseConfig = DATABASE_LIST[databaseName]

        if databaseConfig['adapter'] != "mysql":
                raise Exception("Session is not suported by the {} adapter".format(databaseConfig['adapter']))
       
        class Entity : pass
        entityObject = Entity()
        entityObject.database = databaseName
        databaseObjectRef = cls.__getDatabaseConnection(entityObject)
        return databaseObjectRef.getSession()




    @classmethod
    def create(cls,entityInstance,databaseSession=None):
        """
        Create the entity instance in database

        Attributes
        --------------------------------
        entityInstance : Object
            The instance to entity which will be inserted into databse

        """
        dbConnection = cls.__getDatabaseConnection(entityInstance)
        dbConnection.create(entityInstance,databaseSession=databaseSession)

    
    @classmethod
    def update(cls,entityInstance):
        """
        Update entity in database

        Attributes
        --------------------------------
        entityInstance : object
            The entity that we are trying to update in the database
        database : str (default=billing)
            The database in which entityInstance will be updated



        """
        dbConnection = cls.__getDatabaseConnection(entityInstance)
        dbConnection.update(entityInstance)




    @classmethod
    def rawQuery(cls,entityClass,query,values,responseFormat="json",databaseSession=None):
        dbConnection = cls.__getDatabaseConnection(entityClass)
        data = dbConnection.rawQuery(query,values,databaseSession=databaseSession)
        return data

    @classmethod
    def find(cls,entityClass,whereClause,factoryClass=None,responseFormat="object"):
        """
        Find entity from database

        Attributes
        ---------------------------------
        entityClass : Class
            The superclass entity which we are trying to find the database
        factoryClass : Class
            The factory of from which entity class will be created
        whereClase : dict
            The filtering critera for the database. e.g. { "_id" : "5b72a62ec113fc60c01f524e"}
        database : str (default=billing)
            The database in which find query will happedn
        responseFormat : str(responseFormat="object")
            The reponse format
            if responseFormat=json then dictionary will be returned
            if responseFormat=object then object will be constructed from factoryClass and that will be returned

        Return 
        -----------------------------------
        Array : The data type inside array depends upon the responseFormat

        """
        dbConnection = cls.__getDatabaseConnection(entityClass)
        mongoCursor = dbConnection.find(entityClass,whereClause)
        
        # now we need to take decision if we want to return data a full json or actual object instances
        responseArray = []

        for eachRecord in mongoCursor: 
            if responseFormat == "json":
                responseArray.append(eachRecord)
            else:
                # now we need to check if factory class is given or not
                # factory class is given then creating an instance of that 
                if factoryClass != None:
                    responseArray.append(factoryClass.createInstance(**eachRecord))
                else : 
                    responseArray.append(entityClass(**eachRecord))
        
        return responseArray

    @classmethod
    def createMySQLConnectionDict(cls,mysqlDatabaseConfiguration):
        connectionDict =  {}
        

        connectionDict.update({
            "host": mysqlDatabaseConfiguration['host'] or raiseException("host is required"),
            'port': mysqlDatabaseConfiguration['port'] or raiseException("port is required"),
            'database': mysqlDatabaseConfiguration['database'] or raiseException("database name is required"),
            "user" : mysqlDatabaseConfiguration.get('user',None),
            "password" : mysqlDatabaseConfiguration.get('password',None),
            "charset": 'utf8mb4',
            "cursorclass": pymysql.cursors.DictCursor
        })

        return connectionDict

