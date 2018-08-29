responseList = {
        'MISSING_PARAM':{
            'code'          : 'missingParam',
            'statusCode'    : '400',
            'status'        : 'error',
            'message'       : 'Request is missing {} parameter',
            },
        #####################################################################
        # Authorization Codes
        #####################################################################
        'AUTHORIZATION_TOKEN_NOT_FOUND':{
            'code'          : 'accessDenied',
            'statusCode'    : '401',
            'status'        : 'error',
            'message'       : 'Authorization token is not available in the request',
            },
        'INVALID_CREDENTIALS':{
            'code'          : 'accessDenied',
            'statusCode'    : '401',
            'status'        : 'error',
            'message'       : 'The request has invalid credentials',
            },

        ####################################################################
        # Billable Entity Code
        ####################################################################
        'BILLABLE_ENTITY_CREATE_SUCCESS':{
            'code'          : 'billableEntityCreateSuccess',
            'statusCode'    : '200',
            'message'       : 'Billable Entity successfully Created',
            },
        'BILLABLE_ENTITY_CREATE_FAILED':{
            'code'          : 'billableEntityCreateFailed',
            'statusCode'    : '500',
            'message'       : 'Failed to create billable entity',
            },
        'BILLABLE_ENTITY_UPDATE_SUCCESS':{
            'code'          : 'billableEntityUpdateSuccess',
            'statusCode'    : '200',
            'message'       : 'Billable Entity successfully updated',
            },
        'BILLABLE_ENTITY_UPDATE_FAILED':{
            'code'          : 'billableEntityUpdateFailed',
            'statusCode'    : '500',
            'message'       : 'Failed to update billable entity',
            },
        'BILLABLE_ENTITY_FOUND':{
            'code'          : 'billableEntityFound',
            'statusCode'    : '200',
            'message'       : 'Billable Entity found',
            },
        'BILLABLE_ENTITY_NOT_FOUND':{
            'code'          : 'billableEntityNotFound',
            'statusCode'    : '404',
            'message'       : 'Billable Entity not found',
            },
        ####################################################################
        # Invoice Code
        ####################################################################
        'INVOICE_FOUND': {
            'code': 'invoiceFound',
            'statusCode': '200',
            'message': 'Invoice found',
            },
        'INVOICE_NOT_FOUND': {
            'code': 'invoicNotFound',
            'statusCode': '404',
            'message': 'Invoice not found',
            },
        }
