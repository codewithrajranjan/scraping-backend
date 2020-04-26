#!/bin/bash

# Adding below line as requested by SI for cron jobs
#export BILLING_HOME=/home/alepo/billing/


# Checking if the $BILLING_HOME variable is set or not
if [ -n "$BILLING_HOME" ]
then
    echo "BILLING_HOME is set to : $BILLING_HOME"
else
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    echo "Error : Please set your BILLING_HOME environment variable"
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    exit
fi

cd $BILLING_HOME

export PATH="${BILLING_HOME}/venv/bin:$PATH"


# activating common variables
source "$BILLING_HOME/bin/common.sh"

####################################################################
# checking if billing workers are running or not
####################################################################
echo "Checking if billing is running ..."
sleep $DEFAULT_SLEEP

if (( $(ps -ef | grep $BILLING_SERVICE_NAME | grep $BILLING_HOME | grep -v grep | grep -v watchdog  | wc -l) > 1 ))
then
        echo -e "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	echo    "!Billing is al#ready running"
        echo    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	exit 1
fi
echo -e "--> Billing not running\n"
sleep $DEFAULT_SLEEP


######################################################
# Getting user input data
#####################################################
echo "Enter the Application IP ( Default : $BILLING_SERVICE_IP) "
read USER_BILLING_SERVICE_IP

#  checking if USER_BILLING_SERVICE_IP is not empty then setting BILLING_SERVICE_IP to USER_BILLING_SERVICE_IP
if [[ ! -z "$USER_BILLING_SERVICE_IP" ]]; then
	BILLING_SERVICE_IP=$USER_BILLING_SERVICE_IP
fi

echo "Enter the Application Port ( Default : $BILLING_SERVICE_PORT)"
read USER_BILLING_SERVICE_PORT
#  checking if USER_BILLING_SERVICE_PORT is not empty then setting BILLING_SERVICE_PORT to USER_BILLING_SERVICE_PORT
if [[ ! -z "$USER_BILLING_SERVICE_PORT" ]]; then
	BILLING_SERVICE_PORT=$USER_BILLING_SERVICE_PORT
fi

echo "Enter Application worker count ( Default : $BILLING_WORKER_NUMBER)"
read USER_BILLING_WORKER_NUMBER

#  checking if USER_BILLING_WORKER_NUMBER is not empty then setting BILLING_WORKER_NUMBER to USER_BILLING_WORKER_NUMBER
if [[ ! -z "$USER_BILLING_WORKER_NUMBER" ]]; then
	BILLING_WORKER_NUMBER=$USER_BILLING_WORKER_NUMBER
fi

echo -e "\nStarting $TOTAL_WORKER_TO_SPAWN Billing Th#reads ..."
sleep $DEFAULT_SLEEP
BILLING_LOG=$BILLING_HOME$BILLING_LOG_FILE


gunicorn wsgi:flaskAppInstance \
    --pythonpath=$VIRTUAL_ENV \
    -b $BILLING_SERVICE_IP:$BILLING_SERVICE_PORT \
    -w $BILLING_WORKER_NUMBER --preload >> $BILLING_LOG 2>&1 </dev/null &


echo "##################################################" >> $BILLING_LOG
echo "# Product Name : Billing " >> $BILLING_LOG
echo "# Version 1.0.0.1 " >> $BILLING_LOG
echo "##################################################" >> $BILLING_LOG

echo "Starting Scheduler"
sleep 2
echo "############Starting billing-scheduler.py#############" >>$BILLING_LOG
nohup $BILLING_HOME/venv/bin/python3.4 -u $BILLING_HOME/billing-scheduler.py >> $BILLING_LOG &
echo $! > billing-scheduler-PID.txt 

sleep 5

echo "Please check $BILLING_LOG for more information and debugging"
