__author__ = "Musketeer Liu"


import flask, time, json, subprocess, re, urllib
from flask import request, jsonify
from flask import redirect, render_template, url_for, Response
from flask_cors import CORS


from application import app
from application.forms import InputForm
from datapipeline.pipeline import *
from datapipeline.process import *
from config import *




@app.route('/')
@app.route('/index')
def homepage():
    text = 'Welcome to Yummly Cuisine Prediction API, Redirecting in 3 seconds ...'

    # # Directly return result to the website
    # return text


    # time.sleep(3)

    # print(text)
    # return redirect(url_for('predict'))
    # return redirect('/predict')
    return render_template('index.html', title="Homepage", text = text)


# Using Flask
@app.route('/predict')
def predict():
    form = InputForm()
    if form.validate_on_submit():
        id = form.data('id')
        recipe = form.data('ingredients')
    return render_template('predict.html', title="Cuisine Prediction", form = form)


# Using Flask
@app.route('/result', methods=['POST'])
def result():
    RESULTS = []
    data_bits = request.get_data()
    RESULTS.append(request_prediction_flask(data_bits))
    print('Pipeline Done!')
    return render_template('result.html', results=RESULTS)


# Using React
@app.route('/prediction', methods=['POST'])
def prediction():
    PREDICTION = []

    id = request.args['id']
    recipes = request.args['recipes']

    PREDICTION.append(request_prediction_react(id, recipes))
    print('Pipeline Done!')
    data = {"results": PREDICTION}
    return jsonify(data)


@app.route('/menu')
def menu():
    menu = INGREDIENT_MENU
    return render_template('menu.html', title="Ingredient Menu", menu=menu)


@app.route('/sample')
def ingredient():
    test = {'count': '1st time'}
    body = [
        {
            'id': 397784,
            'ingredients': ['beef brisket', 'sauce tamota', 'carrots', 'white onion', 'fine sea salt']
         },
        {
            'id': 123456,
            'ingredients': ['tvp', 'mutton', 'lemon cake mix', 'sauce tamota', 'jack cheese', 'fine sea salt']
        }
    ]
    return render_template('sample.html', title="Ingredient Sample", test=test, body=body)


# Testing Form Rendering from another URL
@app.route('/extract', methods=['GET', 'POST'])
def extract():
    if request.method == 'POST':
        # print(request.form)
        id = request.form.get('id')
        recipe = request.form.get('ingredients')
    return render_template('extract.html', title="Extracted Data", id=id, recipe=recipe)


# Testing Form Rendering
@app.route('/testing')
def testing():
    form = InputForm()
    if form.validate_on_submit():
        id = form.data('id')
        recipe = form.data['ingredients']
    return render_template('testing.html', form=form)


# Hello World - Just return string
@app.route('/helloworld')
def helloworld():
    return "Cuisine Prediction API!"

