# coding: utf-8

from app import app
from flask import request, render_template, redirect, url_for
from frases import frases
import random

@app.route('/')
def index():
    #Adicionar botão que mude a frase
    frase = random.choice(frases)
    return render_template('index.html', frase=frase.frase)
