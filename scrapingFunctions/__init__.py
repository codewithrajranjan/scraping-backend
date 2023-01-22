from .freecodecamp import FreeCodeCamp
from .eliteDataScience import EliteDataScience
from .techadmin import TechAdmin
from .github_trending_today import GitHubTrendingToday
from .digital_ocean_community import DigitalOceanCommunity
from .geeks_for_geeks import GeeksForGeeksHomePage
from .mongoDBBlog import MongoDBBlog
from .risingStack import RisingStack
from .ditributedPython import DistributedPython
from .datastructureAlgorithm.careerCup import CareerCup
from .videoTutorials.VideoTutorials1337x import VideoTutorial1337x
from .docker.dockerBlog import DockerBlog
from .linuxDistros.centos import CentosBlog
from .linuxDistros.ubuntuBlog import UbuntuBlog
from .medium.MediumTagBased import MediumTagBased
import logging




SCRAPING_FUNCTIONS = [
         # FreeCodeCamp,
         # TechAdmin,
         # GitHubTrendingToday,
         # DigitalOceanCommunity,
         # MongoDBBlog,
         # GeeksForGeeksHomePage,
         # CareerCup,
         # RisingStack,
         # DistributedPython,
         # #VideoTutorial1337x,
         # DockerBlog,
         # CentosBlog,
         # UbuntuBlog,
         MediumTagBased
]



def registerTask(celeryAppInstance):

    registeredTaskDict = {}

    for eachFunction in SCRAPING_FUNCTIONS:
       registeredTaskDict[eachFunction.identifier] = celeryAppInstance.register_task(eachFunction())
       logging.debug(registeredTaskDict)
    
    
    return registeredTaskDict





    
