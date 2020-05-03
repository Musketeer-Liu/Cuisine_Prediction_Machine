import time

from flask import redirect, render_template, url_for, request

from application import app
from application.forms import InputForm




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


@app.route('/predict')
def prediction():
    form = InputForm()
    if form.validate_on_submit():
        id = form.data('ID')
        recipe = form.data('Recipe')
    return render_template('predict.html', title="Cuisine Prediction", form = form)


@app.route('/extract', methods=['GET', 'POST'])
def extract():
    if request.method == 'POST':
        # print(request.form)
        id = request.form.get('id')
        recipe = request.form.get('recipe')
    return render_template('extract.html', title="Extracted Data", id=id, recipe=recipe)


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


@app.route('/testing')
def testing():
    form = InputForm()
    if form.validate_on_submit():
        id = form.data('ID')
        recipe = form.data['Recipe']
    return render_template('testing.html', form=form)


# Hello World
@app.route('/helloworld')
def helloworld():
    return "Cuisine Prediction API!"








