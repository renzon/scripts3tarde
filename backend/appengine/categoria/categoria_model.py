# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.base import Form, StringField, IntegerField


class Categoria(ndb.Model):
    nome = ndb.StringProperty(required=True)
    quantidade = ndb.IntegerProperty(required=True)

class CategoriaForm(Form):
    nome=StringField(required=True)
    quantidade=IntegerField(required=True,lower=0)