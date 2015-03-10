# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def salvar(nome, sobrenome):
    dct = {'name': nome, 'lastname': sobrenome}
    return TemplateResponse(dct, '/usuario/ola.html')


@login_not_required
@no_csrf
def index():
    return TemplateResponse(template_path='/usuario/usuario_form.html')
