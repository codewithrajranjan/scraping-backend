from .freecodecamp import FreeCodeCamp
from .eliteDataScience import EliteDataScience
from .techadmin import TechAdmin
from .freecodecamp_python_latest import FreeCodeCampPythonLatest
from .freecodecamp_nodejs_latest import FreeCodeCampNodeJSLatest
from .github_trending_today import GitHubTrendingToday
from .digital_ocean_community import DigitalOceanCommunity
from .geeks_for_geeks import GeeksForGeeks

SCRAPING_FUNCTIONS = [
        #FreeCodeCamp,
        #TechAdmin,
        #FreeCodeCampPythonLatest,
        #FreeCodeCampNodeJSLatest,
        #GitHubTrendingToday,
        DigitalOceanCommunity
        #GeeksForGeeks
]



def registerTask(celeryAppInstance):

    registeredTaskDict = {}

    for eachFunction in SCRAPING_FUNCTIONS:
       registeredTaskDict[eachFunction.identifier] = celeryAppInstance.register_task(eachFunction())

    return registeredTaskDict





    
