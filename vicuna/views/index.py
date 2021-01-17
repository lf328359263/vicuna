# -*- coding: UTF-8 -*-
from flask import current_app, Blueprint, render_template
bp = Blueprint('hello', __name__, url_prefix='/hello')


@bp.route('/')
def index():
    return 'Hello World!'
