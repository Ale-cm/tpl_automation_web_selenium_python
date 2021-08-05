#INFO: nombres cortos para controlar desde interactivo

def es(sel):
	global browser
	el= browser.find_element_by_css_selector(sel)
	return el

def cn(name):
	global browser
	el= browser.find_element_by_css_selector(f'[name="{name}"]')
	el.click()
	return el

def ca(name):
	global browser
	el= browser.find_element_by_css_selector(f'[aria-label="{name}"]')
	el.click()
	return el

def ct(name):
	global browser
	el= browser.find_element_by_xpath(f"//*//*[text()='{name}']")
	el.click()
	return el

def kn(name,txt):
	global browser
	txt2= txt.replace('\n',Keys.ENTER)
	el= cn(name)
	el.send_keys(txt2)
	return el


