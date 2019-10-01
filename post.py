# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:03:05 2019

@author: CTA
"""

from  data import obtener_elementos, listar_items
ORIGEN_DATA_POST = 'data/posts.json'

def listar_post(post):
    listar_items(post)
    
def obtener_post(fuente):
    return obtener_elementos(fuente)

def ver_posts_de_usuarios(usuarios, num_post):
    for usuario in usuarios:
        ver_post_de_usuario(usuario, num_post)      

def ver_post_de_usuario(usuario):
    data = None
    post_usuario = obtener_post(ORIGEN_DATA_POST)
    if post_usuario is not None:
        data = [post for post in post_usuario if post['userId'] == usuario]
    return data



