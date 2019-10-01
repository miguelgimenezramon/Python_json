# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:41:42 2019

@author: CTA
"""

import json

def obtener_elementos(json_file):
     with open(json_file, 'r') as fichero_report: #Mejor forma de abrir ficheros no es necesario cerrarlos con a append con wt write
           items = json.load(fichero_report)
           return items
       
def listar_items(items):
    for item in items:
        print(item)        
             