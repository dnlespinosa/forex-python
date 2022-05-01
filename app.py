from flask import Flask, request, render_template, redirect, flash, jsonify, session
from forex_python.converter import CurrencyRates

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chickens'
c = CurrencyRates()

@app.route('/')
def home():
    rates = c.get_rates('USD')
    return render_template('index.html', rates=rates)