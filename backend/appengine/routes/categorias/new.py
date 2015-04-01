# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.categoria_model import Categoria
from config.template_middleware import TemplateResponse
from routes import categorias
from tekton.gae.middleware.redirect import RedirectResponse


def salvar(nome, quantidade):
    erros={}
    if nome=='':
        erros['nome']='Campo Obrigatório'
    try:
        quantidade = int(quantidade)
    except:
        erros['quantidade']='Precisa ser um número inteiro'
    if not erros:
        categoria = Categoria(nome=nome, quantidade=int(quantidade))
        categoria.put()
        return RedirectResponse(categorias)
    else:
        valores={'nome':nome,'quantidade':quantidade}
        ctx={'categoria':valores,'erros':erros}
        return TemplateResponse(ctx,'categorias/categoria_form.html')