# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:50:08 2019

@author: CTA
"""
from data import obtener_elementos, obtener_elementos_request
import random

def obtener_usuarios(fuente):
    return obtener_elementos(fuente)

def obtener_usuarios_ramdon(fuente):
    #items = obtener_elementos(fuente)
    usuario = random.choice(fuente)
    #  id_user_aleatorio = random.choice(list(map(lambda u:u['id'],lista_usuarios)))
    return usuario

def obtener_usuarios_ramdon_request(url):
    items = obtener_elementos_request(url)
    usuario = obtener_usuarios_ramdon(items)
    return usuario
    