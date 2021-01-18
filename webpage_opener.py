from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging
from datetime import datetime

logging.basicConfig(filename=r'C:\Users\Bulka\Documents\Python\Python_scripts\webpage_opener', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)
#logger = logging.getLogger()

try:
    logger.info("Starting the process")
    # Sets the path to the driver
    PATH = r"C:\Users\Bulka\Documents\Python\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # Point the driver to the relevant web page
    driver.get("https://www.torrentleech.org/")

    username = driver.find_element_by_name("username")  # Looks for the relevant element in the page source
    username.send_keys("bulka20")  # places my input inside the element
    username.send_keys(Keys.TAB)  # Hit TAB once done
    time.sleep(3)
    password = driver.find_element_by_name("password")
    password.send_keys("TimeCube2020")
    time.sleep(3)
    password.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.quit()
    logger.info("Today was a good day")
except Exception as e:
    logger.error(e)
