import requests
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
requests.post
class RequestService:
    """ Module to contact third party system using http protocol
    """
    def __int__():
        pass
     

    @classmethod
    def get(cls,url,queryParams={},headers={}):
        auth = headers.get('auth',None) 
        logging.debug("Calling url : {}".format(url))
        response = requests.get(url, params=queryParams, headers=headers, auth=auth)
        return response

    @classmethod
    def getFromSelenium(cls,url,queryParams={},headers={}):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-infobars')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-gpu")
        options.add_argument('--no-sandbox')
        options.add_argument('--incognito')
        options.add_argument("--window-size=1920x1080");
        options.add_argument('--remote-debugging-port=9222')
        options.binary_location = "/opt/google/chrome/google-chrome"
        service = Service(executable_path="/home/selftuts/workspace/scraper/scraping-backend/scraping-backend/utils/chromedriver")
        driver =  webdriver.Chrome(service=service,options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'html.parser')
        return soup





if __name__ == "__main__":
    RequestService.getFromSelenium("https://medium.com/tag/nodejs/latest/")