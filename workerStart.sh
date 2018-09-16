source venv/bin/activate
celery worker -c 1 -A worker.celeryApp --loglevel=info 
