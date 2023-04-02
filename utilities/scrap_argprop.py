import requests
import urllib.request
import re

def scrapingArgenProp(cantAmb, barrio, precioMin, precioMax):
    url = "https://www.argenprop.com/departamento-alquiler-barrio-" + str(barrio).replace(" ","-") + "-"+ str(cantAmb) + "-ambientes-"+str(precioMin)+"-"+str(precioMax)+"-pesos"
    print(url)
    
    response = urllib.request.urlopen(url)    
    html_content = response.read().decode('utf-8')
    links = re.findall(r'/departamento-en-alquiler-en-[\s\S]*?"', html_content)
    links = [link for link in links]
    
    new_list = []
    
    for item in links:
           new_list.append("https://www.argenprop.com" + item[:-1])

    links = new_list
    return links

scrapingArgenProp(2, "Villa Crespo", 10, 10000000)