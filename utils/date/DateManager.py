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

    @classmethod
    def compareDate(cls,firstDate,secondDate,considerTime=False):
        """ CompareDate method takes two input arguments
            - firstDate(String)
            - secondDate(String)

            dateDiff(inSeconds) = firstDate-secondDate

            return
                - greater than zero if firstDate is greater than secondDate
                - equal to zero if both the dates are equal
                - less than zero if first date is less than zero
        """
        firstDateObject =  datetime.strptime(firstDate,DATE_FORMAT)
        secondDateObject =  datetime.strptime(secondDate,DATE_FORMAT)

        if considerTime == False :
            firstDateObject = firstDateObject.date()
            secondDateObject = secondDateObject.date()

        return (firstDateObject-secondDateObject).total_seconds()

    @classmethod
    def getHumanRedableDateDiff(cls,firstDate,secondDate):

        diffInseconds = cls.compareDate(firstDate,secondDate,considerTime=True)
        
        number =  0

        text = None

        if diffInseconds < 60 : 
            number = diffInseconds
            text = " seconds ago"

        elif diffInseconds > 60 and diffInseconds < 3600 : 
            number = diffInseconds / 60
            text = " minutes ago"

        elif diffInseconds > 3600 and diffInseconds < 86400 : 
            number = diffInseconds / (60 * 60)
            text = " hour ago"


        if text == None : 
            return ""

        number = int(number)
        return "{}{}".format(number,text)


