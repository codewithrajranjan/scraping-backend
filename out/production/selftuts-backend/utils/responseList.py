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
        # Posts 
        ####################################################################
        'POST_NOT_FOUND':{
            'code'          : 'postNotFound',
            'statusCode'    : '404',
            'message'       : 'Post not found',
            },
        'POST_UPDATE_SUCCESS':{
            'code'          : 'postUpdateSuccess',
            'statusCode'    : '200',
            'message'       : 'Successfully updated post',
            },
        'POST_UPDATE_FAILED':{
            'code'          : 'postUpdateFailed',
            'statusCode'    : '500',
            'message'       : 'Failed to update post',
            },
        }
