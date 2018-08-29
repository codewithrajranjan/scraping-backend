import simplejson as json
import sys
import os


cwd = os.getcwd()
config_file = './config/config'
data = json.loads(open('{}.json'.format(config_file)).read())


#########################################################################
# Database related config
#########################################################################
DATABASE_LIST = data['database']
DATABASE_BILLING = DATABASE_LIST['scraping']
DATABASE_RATING = DATABASE_LIST['rating']

#######################################################################
# Logging
######################################################################
LOGLEVEL = data['log_level']
TIMEZONE = data['timezone']




#######################################################################
# Date Time 
#######################################################################
DATE_FORMAT = data['dateFormat']


