from config import BILLING_TIME,PMS_CLIENT,BILLING_PORT
from utils import RequestService
import sys
import datetime, time

print("######################################################################")
print("##################### Scheduler Started ##############################")
print("######################################################################")

billingHour=None
billingMinute=None

#Get BillingTime from config and get the Hours and Minutes from it
billingTime = (str(BILLING_TIME)).split(':')
billingMinute = billingTime[1]
if billingTime[0].startswith('0'):
    billingHour = billingTime[0][1:]
else:
    billingHour = billingTime[0]

sleepTime = 10


while True:
   time.sleep(sleepTime)
   configDefinedbillingHour = int(billingHour)
   configDefinedbillingMinute = int(billingMinute)
   now = datetime.datetime.now()
   year = now.year
   month = int('%02d' % now.month)
   day = int('%02d' % now.day)
   seconds = int('%02d' % now.second)
   microSecond = int('%02d' % now.microsecond)
   systemDate = now
   billingDate = datetime.datetime(year,month,day,configDefinedbillingHour,configDefinedbillingMinute,0,0)
   #print(systemDate)
   #print(billingDate)
   diff = (systemDate-billingDate).total_seconds()
   if diff > 0 and diff < sleepTime + 3:
        print("######################################################################")
        print("########### Billing Started at {} ##############".format(datetime.datetime.now()))
        print("######################################################################")
        pmsURL = PMS_CLIENT.get('connectionString',None)
        if(pmsURL is None):
            raise Exception("pms client connectionString is empty")
        try:
            pmsGetAllpartnerUrl = pmsURL+"/pms/api/v1.0/partner"
            pmsPartnersList = RequestService.get(pmsGetAllpartnerUrl)
            print("Total Billable Enity fetched is  {} ".format(len(pmsPartnersList.get("data"))))
            for eachPartner in pmsPartnersList.get("data"):
                billableEntityId = eachPartner.get("_id")
                print("Calling BillingResourceIdAPI for billableEntityId {} ".format(billableEntityId))
                #BillingResourceIdAPI="http://localhost:{}/billing/api/v1.0/bill/entity/{}?billingExecutionDate=2018-11-26 00:00:00".format(str(BILLING_PORT),billableEntityId)
                BillingResourceIdAPI="http://localhost:{}/billing/api/v1.0/bill/entity/{}".format(str(BILLING_PORT),billableEntityId)
                try : 
                    RequestService.post(BillingResourceIdAPI)
                except Exception as e:
                    print(e)
                    continue

        except Exception as e:
            raise  Exception(e)


 
        time.sleep(sleepTime)
   else : 
       pass
       #print("wating for correct time")

    
