# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:39:58 2019

@author: CTA
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:51:04 2019

@author: CTA
"""

from typing import List
from gestionblog.usuarios import obtener_usuarios, obtener_usuarios_ramdon, obtener_usuarios_ramdon_request
from gestionblog.post import ver_post_de_usuario, ver_posts_de_usuarios, ver_post_de_usuario_request, ver_post_mas_largo
from gestionblog.comentarios import obtener_comentarios_post_request

ORIGEN_DATA_USUARIOS = 'data/usuarios.json'
URL_DATA_USUARIOS = 'https://jsonplaceholder.typicode.com/users'

def main():
    #lista_usuarios = obtener_usuarios(ORIGEN_DATA_USUARIOS)
   # print(ver_post_de_usuario_request(obtener_usuarios_ramdon_request(URL_DATA_USUARIOS)))
    print(obtener_comentarios_post_request(ver_post_mas_largo(ver_post_de_usuario_request(obtener_usuarios_ramdon_request(URL_DATA_USUARIOS)))))
    
    #posts = ver_post_de_usuario(id_user_aleatorio)
    #listar_post(posts)
    #print(lista_usuarios)

    
if __name__ == "__main__":
    print("Arrancamos ...")
    main()
    