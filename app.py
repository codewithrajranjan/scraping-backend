import logging, os, sys
from flask import Flask, jsonify, request
from flask_cors import CORS
from celery import Celery
from flask_mongoengine import MongoEngine
from uuid import uuid4
LOGLEVEL = "DEBUG"
from webargs.flaskparser import parser

@parser.error_handler
def handle_error(error,req,schema):
    raise Exception(error)


import time
#os.environ['TZ'] = TIMEZONE

#setting for logger configuration
logging.basicConfig(level=LOGLEVEL,format='[%(asctime)s - %(lineno)d : %(filename)s - %(levelname)s] - %(message)s')

# This logger is used for general purpose logging
logger = logging.getLogger(__name__)

logging.getLogger('sqlalchemy.pool').setLevel(logging.DEBUG)
# Setting the timezone for python time library
time.tzset()

# creating flask app instance
flaskAppInstance = Flask(__name__)

cors = CORS(flaskAppInstance, resources={r"/api/*": {"origins": "*"}})

flaskAppInstance.config['SECRET_KEY'] = 'top-secret!'

db = None


def bootstrap():
    """
    This is used to bootstrap the application and creates an instance of app and db
    """
    global flaskAppInstance, db
    db = MongoEngine(flaskAppInstance)
    #Returning the instance of app and db
    return flaskAppInstance, db


# This code is executed when you run the app directly using python
# This is used only for debugging purpose and not used in production server
if __name__ == '__main__':
    bootstrap()
    from api import *
    #calling run function
    flaskAppInstance.run(host='0.0.0.0', port=9000, debug=True,use_reloader=True)














