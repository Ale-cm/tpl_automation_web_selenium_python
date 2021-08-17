from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import json



ESTE_DIR= os.path.abspath('.')

def guardar_archivo_json(donde_guardo, datos):
	with open(donde_guardo,'w') as json_file:
		json.dump(datos, json_file)
		
def scrap_un_articulo(url):
	browser.get(url)	
	browser.implicitly_wait(6)
	nombrePro=browser.find_element_by_xpath('//div//h1').text
	precioPro=browser.find_element_by_xpath('//main//div//div//span//meta/following-sibling::span[2]/span[2]').text
	#DBG: print(nombrePro)
	#DBG: print(precioPro)
	return (str(nombrePro),float(precioPro))

def mostrar(productos):
	numElem = len(productos)
	print ("\nNumero de elementos del diccionario = %i" %numElem)
	for k,v in productos.items():
		print('%s -> %s' %(k,v))
		#TO DO: En el dicionario productos pasarle por valor un objeto con los atributos precio(float) y nombre(str)

	time.sleep(5)

profile_dir= ESTE_DIR+'/_data'

options= webdriver.ChromeOptions() 
options.add_argument("user-data-dir="+profile_dir) #Path to your chrome profile
browser= webdriver.Chrome("C:/Users/Alejandro/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=options)

browser.get('https://www.mercadolibre.com.ar/')
browser.refresh()

busqueda=browser.find_element_by_name(f'as_word')
busqueda.send_keys('zapatillas' +Keys.ENTER)

links=browser.find_elements_by_xpath(f'//ol/li/div/div/a[starts-with(@href,"https://")]')

urls=[x.get_attribute('href') for x in links]
datos=[scrap_un_articulo(u) for u in urls]
prod_a_precio={prod:precio for (prod,precio) in datos}
guardar_archivo_json("meli.json",prod_a_precio)
mostrar(prod_a_precio)

browser.quit()