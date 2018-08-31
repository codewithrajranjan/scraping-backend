from flask_restful import Api
from app import flaskAppInstance
from .ScrapingResource import ScrapingResource
from .ScrapingResourceByIdentifier import ScrapingResourceByIdentifier
from .BlogByStatus import BlogByStatus
from .Blogs import Blogs

restServer = Api(flaskAppInstance)

restServer.add_resource(ScrapingResource,"/api/v1.0/scrape")
restServer.add_resource(ScrapingResourceByIdentifier,"/api/v1.0/scrape/identifier/<string:identifier>")

restServer.add_resource(Blogs,"/api/v1.0/blogs")
restServer.add_resource(BlogByStatus,"/api/v1.0/blog/<string:blogId>/status/<string:blogStatus>")
