# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest import TestCase
from base import GAETestCase
from categoria.categoria_model import Categoria
from config.template_middleware import TemplateResponse
from mock import Mock
from routes.categorias.new import salvar
from routes.rest import produtos
from tekton.gae.middleware.redirect import RedirectResponse


class NewTests(GAETestCase):
    def test_sucesso(self):
        resposta = salvar(nome='Notebooks', quantidade='2')
        self.assertIsInstance(resposta, RedirectResponse)
        self.assertEqual('/categorias', resposta.context)
        categorias = Categoria.query().fetch()
        self.assertEqual(1, len(categorias))
        cat = categorias[0]
        self.assertEqual('Notebooks', cat.nome)
        self.assertEqual(2, cat.quantidade)

    def test_erro_validacao(self):
        resposta = salvar()
        self.assertIsInstance(resposta, TemplateResponse)
        self.assert_can_render(resposta)
        self.assertIsNone(Categoria.query().get())
        self.assertDictEqual({u'categoria': {},
                              u'erros': {'quantidade': u'Required field',
                                         'nome': u'Required field'}},
                             resposta.context)

    def test_salvar_produto_erro_json(self):
        resposta_http = Mock()
        resposta = produtos.salvar(resposta_http)
        self.assert_can_serialize_as_json(resposta)
        resposta_http.set_status.assert_called_once_with(400)


mock = Mock()

mock.bizarro(9)
mock.bizarro.assert_called_once_with(9)