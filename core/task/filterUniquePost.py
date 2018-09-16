from worker import celeryApp
from core.post import Post
from database import DatabaseManager
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)




@celeryApp.task
def filterUniquePost(context):
        
        context['uniquePosts'] = []
        postFromScrapingArray = context.get('posts') 

        labelArray = []
        labelBasedDict = {}

        for eachPost in postFromScrapingArray: 
            labelArray.append(eachPost['label'])
            
        whereClause = {
                    "label" : { "$in" : labelArray }
        }
        alreadyExistingPostInDatabase =  DatabaseManager.find(Post,whereClause,responseFormat="json")

        # if the length of all new post and searched post from database is same then 
        # no new post has been updated by the 
        if len(alreadyExistingPostInDatabase) == len(postFromScrapingArray):
            # returning empty array as no new post has been found
            return context

        remaingingPost = []
        # if the length don't match then we need only return new posts
        for eachNewPost in postFromScrapingArray:
            label = eachNewPost['label']
            flag = True
            for eachPostInDatabase in alreadyExistingPostInDatabase:
                if label == eachPostInDatabase['label']:
                    flag = False

            if flag == True :
                remaingingPost.append(eachNewPost)



        # getting post if it is remaining in labelBasedDict
        context['uniquePosts'] = remaingingPost

        logger.info("########################################")
        logger.info("##     Total New Post : {}       #######".format(len(remaingingPost)))
        logger.info("########################################")



        if len(remaingingPost) > 0:
            insertNewPostsInDatabase(remaingingPost)

        return context



def insertNewPostsInDatabase(allPosts):

        for eachPost in allPosts:
            eachPost['status'] = "new"
            DatabaseManager.create(Post(**eachPost))







