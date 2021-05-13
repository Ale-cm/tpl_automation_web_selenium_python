#INFO: como subir un archivo
#VER: http://the-internet.herokuapp.com/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
ESTE_DIR= os.path.abspath('.')

browser = webdriver.Chrome()

browser.get('http://the-internet.herokuapp.com/upload')

browser.save_screenshot('x_borrame.png')

print('Screenshot guardado como x_borrame')

browser.quit()



