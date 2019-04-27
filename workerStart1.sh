#source venv/bin/activate
watchmedo auto-restart -d . -p '*.py' --recursive  -- celery worker -c 4 -A worker.celeryApp --loglevel=info -n worker1
