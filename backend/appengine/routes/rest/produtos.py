# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from categoria.categoria_model import ProdutoForm, Produto
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse


@login_not_required
@no_csrf
def apagar(produto_id):
    key = ndb.Key(Produto, int(produto_id))
    key.delete()
    return JsonUnsecureResponse('') # para setar cabeçalho para aplpication/json


@login_not_required
@no_csrf
def listar():
    form = ProdutoForm()
    produtos = Produto.query_ordenada_por_nome().fetch()
    produtos = [form.fill_with_model(p) for p in produtos]
    return JsonUnsecureResponse(produtos)


@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = ProdutoForm(**propriedades)
    erros = form.validate()
    if not erros:
        produto = form.fill_model()
        produto.put()
        dct = form.fill_with_model(produto)
        return JsonUnsecureResponse(dct)
    _resp.set_status(400)
    return JsonUnsecureResponse(erros)