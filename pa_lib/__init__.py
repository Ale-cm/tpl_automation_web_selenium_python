#INFO: funciones extra para encontrar componentes react

from selenium import webdriver
import unittest
import json

#U: lo que necesita estar cargado en la pagina para que funcione el resto
JS_INIT_LIBS= """
	if (!window.loadJs_withTag_p) {
		window.loadJs_withTag_p= function loadJs_withTag_p(url) {
			var r= document.createElement('script');
			var p= new Promise(cb => { r.onload= (e  => cb(e,r)) });
			r.src = url;
			var firstScriptTag = document.getElementsByTagName('script')[0];
			firstScriptTag.parentNode.insertBefore(r, firstScriptTag);
			return p;
		}
		await Promise.all([
			loadJs_withTag_p('https://cdn.jsdelivr.net/npm/resq@1.10.0/dist/index.js'),
			loadJs_withTag_p('https://unpkg.com/get-xpath@3.0.1/index.umd.js'),
		]);
	}
"""

def find_elements_react(browser, tag, props={}, rootId= 'root', quiereDatos= False):
	"""Devuelve un array de elementos creados en React con el tag especificado, cuyas props coincidan con las recibidas como parámetro.
	Si la aplicación React no está montada en un elemento con id='root' es necesario especificar el rootId.
	Si quiereDatos=True devuelve diccionarios con el elemento y las props.
	"""
	
	e= browser.execute_script(
			JS_INIT_LIBS +	
			f"var quiereDatos={1 if quiereDatos else 0};\nvar els= resq.resq$$('{tag}', document.getElementById('{rootId}') ).byProps({json.dumps(props)});\n" +
			"""
			var r= []; var i; 
			for (i=0; i<els.length;i++) { 
				if (quiereDatos) {
					r.push({element: els[i].node, props: els[i].props, xpath: getXPath(els[i].node)}) 
				}
				else {
					r.push(els[i].node) 
				}
			}
			return r; 
			""",
		)
	#DBG: print(f'find_element_react {e}')
	return e

def find_element_react(browser, tag, props={}, rootId= 'root', quiereDatos= False):
	"""Como find_elements_react pero devuelve solamente el primero"""
	r= find_elements_react(browser, tag, props, rootId, quiereDatos)
	return (None if len(r)==0 else r[0])

class BaseTest(unittest.TestCase):
	"""Una base comun para configurar los tests"""
	def setup_method(self, method):
		self.driver = webdriver.Chrome() #U: podes cambiar por firefox u otro driver #TODO: hacer config
		self.driver.implicitly_wait(10) #A: esperar 10 a que este disponible elemento buscado
		self.vars = {}
		self.browser= self.driver #A: por comodidad, me gusta más escribir browser pero selenium ide genera driver

	def teardown_method(self, method):
		self.driver.quit()
 
