# coding: utf-8

from app import app
from flask import request, render_template, redirect, url_for

@app.route('/')
def index():
    frase = "OLÁ!"
    return render_template('index.html', frase=frase)
