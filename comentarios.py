# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:55:33 2019

@author: CTA
"""
from data import obtener_elementos_request
URL_DATA_COMMENTS = "https://jsonplaceholder.typicode.com/comments"

def obtener_comentarios_post_request(post):
    comentarios = None
    if post is not None:
        postId = post['id']
        comentarios = obtener_elementos_request(URL_DATA_COMMENTS +  f"?postId={postId}")
    return comentarios
