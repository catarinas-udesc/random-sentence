# coding: utf-8

from app import app
from flask import request, render_template, redirect, url_for
from frases import frases
import random

@app.route('/')
def index():
    return render_template('index.html', frase=random.choice(frases))
