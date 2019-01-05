from .freecodecamp import FreeCodeCamp
from .eliteDataScience import EliteDataScience
from .techadmin import TechAdmin
from .freecodecamp_python_latest import FreeCodeCampPythonLatest
from .freecodecamp_nodejs_latest import FreeCodeCampNodeJSLatest
from .github_trending_today import GitHubTrendingToday
from .digital_ocean_community import DigitalOceanCommunity
from .geeks_for_geeks import GeeksForGeeksHomePage
from .mongoDBBlog import MongoDBBlog
from .risingStack import RisingStack
from .ditributedPython import DistributedPython
from .datastructureAlgorithm.mediumDSALGOLatest import MediumDSALGOLatest
from .datastructureAlgorithm.careerCup import CareerCup




SCRAPING_FUNCTIONS = [
       # FreeCodeCamp,
       # #TechAdmin,
       # FreeCodeCampPythonLatest,
       # FreeCodeCampNodeJSLatest,
       # GitHubTrendingToday,
       # DigitalOceanCommunity,
       # MongoDBBlog,
        GeeksForGeeksHomePage,
        MediumDSALGOLatest,
        CareerCup
       # RisingStack,
       # DistributedPython
]



def registerTask(celeryAppInstance):

    registeredTaskDict = {}

    for eachFunction in SCRAPING_FUNCTIONS:
       registeredTaskDict[eachFunction.identifier] = celeryAppInstance.register_task(eachFunction())

    return registeredTaskDict





    
