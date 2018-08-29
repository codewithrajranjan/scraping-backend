from flask_restful import Api
from app import flaskAppInstance
from .ScrapingResource import ScrapingResource

restServer = Api(flaskAppInstance)

restServer.add_resource(ScrapingResource,"/api/v1.0/scrape")

