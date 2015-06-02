# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest import TestCase


def soma(param, param1):
    return param+param1


class SomaTests(TestCase):
    def testes_soma(self):
        resultado = soma(1, 2)
        self.assertEqual(3, resultado)
        self.assertEqual(3.5, soma(0.5, 3))
