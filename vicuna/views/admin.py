# -*- coding: UTF-8 -*-
from flask import current_app, Blueprint, render_template
bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def index():
    return 'Hello World!'
