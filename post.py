# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:03:05 2019

@author: CTA
"""

from  data import obtener_elementos, listar_items, obtener_elementos_request
ORIGEN_DATA_POST = 'data/posts.json'
URL_DATA_POS = 'https://jsonplaceholder.typicode.com/posts'

def listar_post(post):
    listar_items(post)
    
    
def obtener_post(fuente):
    return obtener_elementos(fuente)

def ver_posts_de_usuarios(usuarios, num_post):
    for usuario in usuarios:
        ver_post_de_usuario(usuario, num_post)
        
def ver_post_de_usuario_request(usuario):
    items = None
    if usuario is not None:
        userId = usuario['id']
        items = obtener_elementos_request(URL_DATA_POS +  f"?userId={userId}")   
    return items   

def ver_post_de_usuario(usuario):
    data = None
    post_usuario = obtener_post(ORIGEN_DATA_POST)
    if post_usuario is not None:
        data = [post for post in post_usuario if post['userId'] == usuario]
    return data

def ver_post_mas_largo(posts):
    post = None
    if posts is not None:
        posts.sort(key = lambda p:len(p['body'].split()), reverse=True)
        post = posts[0]
    return post
            

