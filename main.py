""" main.py is the top level script.

Return "Hello World" at the root URL.
"""

import os
import sys

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import render_template
app = Flask(__name__.split('.')[0])


@app.route('/')
@app.route('/<name>')
def hello(name=None):
  """ Return hello template at application root URL."""
  return render_template('home.html')

@app.route('/catwalk')
def CatWalk(name=None):
  """ Return me template at application /me URL."""
  return render_template('CatWalk.html')
@app.route('/madlibs')
def madlibs(name=None):
  """ Return me template at application /me URL."""
  return render_template('madlibs.html')
