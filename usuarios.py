# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:50:08 2019

@author: CTA
"""
from data import obtener_elementos
import random

def obtener_usuarios(fuente):
    return obtener_elementos(fuente)

def obtener_usuarios_ramdon(fuente):
    items = obtener_elementos(fuente)
    usuario = random.choice(items)
    return usuario
