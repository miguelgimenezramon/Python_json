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
from usuarios import obtener_usuarios, obtener_usuarios_ramdon
from post import ver_post_de_usuario, ver_posts_de_usuarios, listar_post
import random

ORIGEN_DATA_USUARIOS = 'data/usuarios.json'


def main():
    lista_usuarios = obtener_usuarios(ORIGEN_DATA_USUARIOS)
    id_user_aleatorio = random.choice(list(map(lambda u:u['id'],lista_usuarios)))
    posts = ver_post_de_usuario(id_user_aleatorio)
    listar_post(posts)
    #print(lista_usuarios)

    
if __name__ == "__main__":
    print("Arrancamos ...")
    main()
    