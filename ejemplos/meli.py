from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


ESTE_DIR= os.path.abspath('.')
profile_dir= ESTE_DIR+'/_data'

options= webdriver.ChromeOptions() 
options.add_argument("user-data-dir="+profile_dir) #Path to your chrome profile
browser= webdriver.Chrome("C:/Users/Alejandro/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=options)

browser.get('https://www.mercadolibre.com.ar/')
browser.refresh()

busqueda=browser.find_element_by_name(f'as_word')
busqueda.send_keys('zapatillas' +Keys.ENTER)
urls=[]
urls=browser.find_elements_by_xpath(f'//ol/li/div/div/a[starts-with(@href,"https://")]')
url=[]
i=0
productos=dict()
for	x in urls:
	#DBG: print(x.get_attribute('href'))
	url.append(x.get_attribute('href'))
	#DBG: i+=1
	#DBG: print(i)

for ii in url:
	browser.get(ii)
	browser.implicitly_wait(6)
	nombrePro=browser.find_element_by_xpath('//div//h1').text
	precioPro=browser.find_element_by_xpath('//main//div//div//span//meta/following-sibling::span[2]/span[2]').text
	#DBG: print(nombrePro)
	#DBG: print(precioPro)
	productos.setdefault(str(nombrePro),float(precioPro))

numElem = len(productos)
print ("\nNumero de elementos del diccionario = %i" %numElem)

for k,v in productos.items():
    print('%s -> %s' %(k,v))
	#TO DO: En el dicionario productos pasarle por valor un objeto con los atributos precio(float) y nombre(str)
time.sleep(5)
browser.quit()