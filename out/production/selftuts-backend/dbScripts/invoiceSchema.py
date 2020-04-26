from config import DATABASE_RATING
from database import DatabaseManager
import pymysql.cursors


connectionDict = DatabaseManager.createMySQLConnectionDict(DATABASE_RATING)


connection = pymysql.connect(**connectionDict)

#TODO
# invoice -invoices
# entityId ====> to billingEntityId
# amoutn double



try:
    with connection.cursor() as cursor:
        # first see it table exists

        try :
            sql = "drop table if exists `invoices`"
            cursor.execute(sql)
            connection.commit()
        except Exception as e:
            logger.error("Not table with name invoices found : Error -  {}".format(str(e)))

        sql = "CREATE TABLE `invoices` ( \
                `id` int(11) NOT NULL AUTO_INCREMENT, \
                `tenantId` varchar(255) NOT NULL, \
                `transactionId` varchar(255) NOT NULL, \
                `billingEntityId` varchar(255) NOT NULL, \
                `invoiceNumber` varchar(255) NOT NULL, \
                `createdAt` varchar(20) NOT NULL, \
                `paymentDueDate` varchar(20) NOT NULL, \
                `totalAmount` int(11) NOT NULL, \
                `latePaymentCharges` int(11) NOT NULL, \
                PRIMARY KEY (`id`) \
               )"

        cursor.execute(sql)
        connection.commit()



finally:
    connection.close()
