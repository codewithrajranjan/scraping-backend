#!/bin/bash

# This file contains all the common variables that will be needed in all scripts
###########################################
# Common variable in all script
###########################################
DEFAULT_SLEEP=1


############################################
# Billing related variables
###########################################
BILLING_SERVICE_NAME=gunicorn
BILLING_SERVICE_IP=0.0.0.0
BILLING_SERVICE_PORT=`cat $BILLING_HOME/config/config.json | jq '.port' `
BILLING_WORKER_NUMBER=4
BILLING_LOG_FILE=`cat $BILLING_HOME/config/config.json | jq '.logs.file'  | tr -d '"' | sed 's/.//'`

#echo `cat /home/alepo/workspace/interConnectBilling/billing/config/config.json | jq '.logs.file'`
#echo $BILLING_LOG_FILE
#echo $BILLING_SERVICE_PORT
