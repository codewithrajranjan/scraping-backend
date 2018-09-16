from celery import Celery

celeryApp = Celery('tasks', broker='pyamqp://admin:password@localhost//')

from scrapingFunctions import registerTask
from database import DatabaseManager

registerTask(celeryApp)
from core.task import *

from celery.signals import celeryd_init, worker_process_init


@worker_process_init.connect()
def configure_worker(conf=None, **kwargs):
    global db

    db = DatabaseManager()


