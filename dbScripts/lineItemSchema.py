from config import DATABASE_RATING
from database import DatabaseManager
import pymysql.cursors


connectionDict = DatabaseManager.createMySQLConnectionDict(DATABASE_RATING)


connection = pymysql.connect(**connectionDict)



#TODO
# change table name to billedlineitems
# change transactioId to internalBillId
# amount float/double check with current billing  - default precion
# identifier to policyIdentifier
# createdAt - DATETIME

try:
    with connection.cursor() as cursor:
        # first see it table exists

        try :
            sql = "drop table if exists `lineitem`"
            cursor.execute(sql)
            connection.commit()
        except Exception as e:
            logger.error("Not table with name invoice found : Error -  {}".format(str(e)))

        sql = "CREATE TABLE `lineitem` ( \
                `id` int(11) NOT NULL AUTO_INCREMENT, \
                `transactionId` varchar(255) NOT NULL, \
                `label` varchar(255) NOT NULL, \
                `description` varchar(255) DEFAULT NULL, \
                `quantity` varchar(255) DEFAULT NULL, \
                `unit` varchar(255) DEFAULT NULL, \
                `amount` varchar(255) NOT NULL, \
                `identifier` varchar(255) NOT NULL, \
                `createdAt` varchar(255) DEFAULT NULL, \
                `invoiceId` varchar(255) NOT NULL, \
                 PRIMARY KEY (`id`) \
               )"

        cursor.execute(sql)
        connection.commit()



finally:
    connection.close()
