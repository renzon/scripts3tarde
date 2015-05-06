# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.categoria_model import Categoria, ProdutoForm, Produto
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@no_csrf
def index(categoria_selecionada=None):
    ctx={'categorias':Categoria.query_ordenada_por_nome().fetch(),
         'salvar_path':to_path(salvar),
         'pesquisar_path': to_path(index)}
    if categoria_selecionada is None:
        ctx['categoria_selecionada']= None
    else:
        ctx['categoria_selecionada']=Categoria.get_by_id(int(categoria_selecionada))
    return TemplateResponse(ctx, 'produtos/produto_home.html')


def salvar(**propriedades):
    form = ProdutoForm(**propriedades)
    erros = form.validate()
    if not erros:
        produto = form.fill_model()
        produto.put()
    return RedirectResponse(index)