from flask_restful import Resource
import logging
import traceback


class ProjectAPI(Resource):
    
    def get(self):
        try: 
            
            dataToReturn  = {
                    'topic' : [
                        {'key': 'Array','value':'array'},
                        {'key': 'String','value':'string'},
                        {'key': 'Binary Search Tree','value':'bst'},
                        {'key': 'Sorting','value':'sorting'},
                        {'key': 'Math','value':'math'},
                        {'key': 'Stack','value':'stack'},
                        {'key': 'System Design','value':'system-design'},
                        {'key': 'Bit Programming','value':'bit'},
                        {'key': 'Binary Tree','value':'binary-tree'}

                    ]
            }
            return {'message':'project data returned successfully','data': dataToReturn},200

        except Exception as e:

            logging.error(e)
            traceback.print_exc()
            return {'message': "Failed to return project data"},500



    def options(self):
        return {'Allow' : 'GET, POST,PUT, DELETE' }, 200, \
               {
                        'Access-Control-Allow-Origin': '*',
                        'Access-Control-Allow-Headers': 'Authorization,Content-Type, Auth, Token, Access-Token, Access_Token, AccessToken, Code',
                        'Access-Control-Allow-Methods': 'PUT,GET,POST,DELETE'
                }



