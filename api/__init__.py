from flask_restful import Api
from app import flaskAppInstance
from .scraping import ScrapingResource
from .scraping import ScrapingResourceByIdentifier
from .BlogByStatus import BlogByStatus
from .Blogs import Blogs
from .BlogTagsAPI import BlogTagsAPI
from .question.QuestionAPI import QuestionAPI
from .question.QuestionByIdAPI import QuestionByIdAPI
from .project import ProjectAPI
from .identifier import Identifier

restServer = Api(flaskAppInstance)

restServer.add_resource(ScrapingResource,"/api/v1.0/scrape")
restServer.add_resource(ScrapingResourceByIdentifier,"/api/v1.0/scrape/identifier/<string:identifier>")

restServer.add_resource(Blogs,"/api/v1.0/blogs")
restServer.add_resource(BlogByStatus,"/api/v1.0/blog/<string:blogId>/status/<string:blogStatus>")

restServer.add_resource(BlogTagsAPI,"/api/v1.0/tag")



############################################################
# Question related apis
##########################################################
restServer.add_resource(QuestionAPI,"/api/v1.0/question")
restServer.add_resource(QuestionByIdAPI,"/api/v1.0/question/id/<string:questionId>")



#########################################################
# Project related apis
###########################################################
restServer.add_resource(ProjectAPI,"/api/v1.0/project")


############################################################
# post identifier related api
############################################################
restServer.add_resource(Identifier,"/api/v1.0/identifier")







