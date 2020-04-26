#!/bin/bash

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

# activating common variables
source "$BILLING_HOME/bin/common.sh"
BILLING_LOG=$BILLING_HOME$BILLING_LOG_FILE
###############################################
# checking if billing is running or not
###############################################
if (( $(ps -ef | grep $BILLING_SERVICE_NAME | grep $BILLING_HOME |wc -l) > 1 ))
then
	echo "Shutting down the service"
	echo "$(date) Shutting down the service">> $BILLING_LOG
	echo "`ps -ef | grep $BILLING_SERVICE_NAME | grep $BILLING_HOME ` " >> $BILLING_LOG
	ps -ef | grep $BILLING_SERVICE_NAME | grep $BILLING_HOME | awk {'print $2'} | xargs kill -9
        #Stop the billing-scheduler  services    
        kill -9 `cat billing-scheduler-PID.txt`
        rm billing-scheduler-PID.txt
        sleep 2

else
	echo "Service is not running"
fi
