# -*- coding: utf-8 -*-

from . import home

@home.route('/', methods=['GET', 'POST'])
def index():
    return '''<h1>Hello World</h1>'''