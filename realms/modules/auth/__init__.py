from __future__ import absolute_import

from flask import request, flash, redirect
from flask_login import login_url

from ... import login_manager

modules = set()

@login_manager.unauthorized_handler
def unauthorized():
    if request.method == 'GET':
        flash('Please log in to access this page')
        return redirect(login_url('auth.login', request.url))
    else:
        return dict(error=True, message="Please log in for access."), 403
