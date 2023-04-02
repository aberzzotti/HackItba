import requests
import urllib.request
import re

def scrapingClarinProp(cantAmb, barrio, precioMin, precioMax):
    if cantAmb == 1:
       url = "https://www.inmuebles.clarin.com/departamento-alquiler-barrio-" + str(barrio) +"-localidad-capital-federal-" + str(cantAmb) + "-ambiente-" + str(precioMin) +"-" + str(precioMax) +"-pesos"
    else:
       url = "https://www.inmuebles.clarin.com/departamento-alquiler-barrio-" + str(barrio) +"-localidad-capital-federal-" + str(cantAmb) + "-ambientes-" + str(precioMin) +"-" + str(precioMax) +"-pesos"
    print(url)
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')

    response = urllib.request.urlopen(url)    
    html_content = response.read().decode('utf-8')
    links = re.findall(r'/departamento-en-alquiler-en-[\s\S]*?"', html_content)
    links = [link for link in links]
    
    new_list = []
    
    for item in links:
           new_list.append("https://www.inmuebles.clarin.com" + item[:-1])

    links = new_list
    return links

