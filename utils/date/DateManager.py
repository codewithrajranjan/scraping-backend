import logging
from config import DATE_FORMAT
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

class DateManager:

    @classmethod
    def addBillCycle(cls,dateInString,billCycle):
        # making date object from the string and the date format
        dateObject =  datetime.strptime(dateInString,DATE_FORMAT)

        #initializing the new date object
        newDateObject = None

        if billCycle == "MONTHLY_ANNIVERSARY":
            # adding one month to the date object
            newDateObject = dateObject + relativedelta(months=+1)

        elif billCycle == "WEEKLY_ANNIVERSARY":
            # adding seven days to the dateobject
            newDateObject = dateObject + timedelta(days=+7)

        else : 
            raise "{} billCycle is not supported by date DateManager".format(billCycle)

        # returning the string format of the date
        return newDateObject.strftime(DATE_FORMAT)

    @classmethod
    def getTodaysDate(cls):
        now = datetime.now()
        return now.strftime(DATE_FORMAT)

