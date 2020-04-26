import simplejson as json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
config_file = "{}{}".format(dir_path,"/config.json");
data = json.loads(open(config_file  ).read())


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


