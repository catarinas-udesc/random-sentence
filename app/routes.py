# coding: utf-8

from app import app
from flask import request, render_template, redirect, url_for, jsonify
from frases import frases
import random

@app.route('/')
def index():
    frase = random.choice(frases)
    return render_template('index.html', frase=frase)

@app.route('/frase')
def api_frase():
    frase = random.choice(frases)
    return jsonify({
        "frase": frase
    })
