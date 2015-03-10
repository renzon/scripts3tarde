# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router


@login_not_required
@no_csrf
def salvar(nome, sobrenome):
    path = router.to_path(index)
    dct = {'name': nome,
           'lastname': sobrenome,
           'usuario_path': path
    }
    return TemplateResponse(dct, '/usuario/ola.html')


@login_not_required
@no_csrf
def index():
    path = router.to_path(salvar)
    ctx = {'usuarios': ['Renzo', 'Jão', 'Paulo', 'Fabiana'],
           'usuario_path': path}
    return TemplateResponse(ctx, template_path='/usuario/usuario_form.html')
