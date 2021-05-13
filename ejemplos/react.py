#FROM: https://pypi.org/project/selenium/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from pa_lib import find_element_react

browser = webdriver.Chrome()

browser.get('http://localhost:3000')

elUsuario = browser.find_element_by_css_selector('#email') 
elUsuario.send_keys('admin' + Keys.TAB)

elPass = browser.find_element_by_css_selector('#password') 
elPass.send_keys('secreto' + Keys.TAB)

elBtnLogin = browser.find_element_by_css_selector('button[type="submit"]') 
elBtnLogin.click()

browser.implicitly_wait(10) #A: esperar 10 a que este disponible elemento buscado
elBtnMenu = browser.find_element_by_css_selector('button[aria-label="open drawer"]')
elBtnMenu.click()

elItemQueHago= browser.find_element_by_link_text('¿Qué hago?')
elItemQueHago.click()

print(f'{elItemQueHago}')

#VER: https://devhints.io/xpath
elWifi= browser.find_element_by_xpath("//label//*[text()='WiFi']") #A: que diga WiFi y este dentro de un label
elWifi.click()

#browser.execute_script('alert("Hola")')
r= browser.execute_script('return new Date()')
print(f'En python {r}');

e= find_element_react(browser, 'ListItemText', {'primary': 'Charlas'}, quiereDatos= True);
e= find_element_react(browser, 'ListItemText', quiereDatos= True);
print(f'En python {e}');

#browser.quit()

