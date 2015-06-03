# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api.app_identity.app_identity import get_default_gcs_bucket_name
from google.appengine.ext import blobstore
from blob_app import blob_facade
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@login_not_required
@no_csrf
def index():
    pass


@login_not_required
def upload(_handler, files):
    blob_infos = _handler.get_uploads('files')
    blob_facade.save_blob_files_cmd(blob_infos).execute()
    return RedirectResponse(index)


@login_not_required
@no_csrf
def form():
    upload_path = to_path(upload)
    bucket = get_default_gcs_bucket_name()
    url = blobstore.create_upload_url(upload_path, gs_bucket_name=bucket)
    ctx = {'salvar_path': url}
    return TemplateResponse(ctx, 'upload_form.html')

