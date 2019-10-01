# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:41:42 2019

@author: CTA
"""

import json
import requests

def obtener_elementos(json_file):
     with open(json_file, 'r') as fichero_report: #Mejor forma de abrir ficheros no es necesario cerrarlos con a append con wt write
           items = json.load(fichero_report)
           return items
       
def listar_items(items):
    for item in items:
        print(item) 
        
        
def obtener_elementos_request(url):
    response = requests.get(url)
    resulset = response.json()
    return resulset
    
             