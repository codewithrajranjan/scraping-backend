from config import DATABASE_RATING
from database import DatabaseManager
import pymysql.cursors


connectionDict = DatabaseManager.createMySQLConnectionDict(DATABASE_RATING)


connection = pymysql.connect(**connectionDict)



try:
    with connection.cursor() as cursor:
        # first see it table exists

        try : 
            sql = "drop table if exists `ratingedr`"
            cursor.execute(sql)
            connection.commit()
        except Exception as e:
            logger.error("Not table with name edr found : Error -  {}".format(str(e)))

        sql = "CREATE TABLE `edr` ( \
               `id` int(11) NOT NULL AUTO_INCREMENT, \
               `transactionId` varchar(255) DEFAULT NULL , \
               `tenantId` varchar(255) NOT NULL, \
               `entityId` varchar(255) NOT NULL, \
               `amount` int(11) NOT NULL, \
               `serviceType` varchar(255) NOT NULL, \
               `direction` varchar(255) NOT NULL, \
               `duration` int(11) NOT NULL, \
               `createdAt` datetime NOT NULL, \
                PRIMARY KEY (`id`) \
               )"

        cursor.execute(sql)
        connection.commit()



finally:
    connection.close()
