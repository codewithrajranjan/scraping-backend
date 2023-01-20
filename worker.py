from celery import Celery
import os
import logging

#RABBITMQ_SERVER_STRING=os.environ["RABBITMQ_SERVER_STRING"]
#RABBITMQ_SERVER_STRING = "amqp://user:password@master.cluster.local:30163/"
RABBITMQ_SERVER_STRING = "amqp://guest:guest@localhost:5672/"

logging.debug(RABBITMQ_SERVER_STRING)


celeryApp = Celery('tasks', broker=RABBITMQ_SERVER_STRING)

from scrapingFunctions import registerTask
from database import DatabaseManager

registerTask(celeryApp)
from core.task import *

from celery.signals import celeryd_init, worker_process_init


@worker_process_init.connect()
def configure_worker(conf=None, **kwargs):
    global db

    db = DatabaseManager()


