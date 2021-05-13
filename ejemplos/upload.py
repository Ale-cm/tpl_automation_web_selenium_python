#INFO: como subir un archivo
#VER: http://the-internet.herokuapp.com/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
ESTE_DIR= os.path.abspath('.')

browser = webdriver.Chrome()

browser.get('http://the-internet.herokuapp.com/upload')

elFile= browser.find_element_by_css_selector('#file-upload')
elFile.send_keys(f'{ESTE_DIR}/img/podemos_regadera_512x512.png')

elBtn= browser.find_element_by_css_selector('#file-submit')
elBtn.click()




