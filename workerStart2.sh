source venv/bin/activate
celery worker -c 4 -A worker.celeryApp --loglevel=info -n worker2
