import time

from flask import redirect, render_template, url_for

from application import app
from application.forms import InputForm




# Hello World
@app.route('/helloworld')
def helloworld():
    return "Cuisine Prediction API!"


@app.route('/')
@app.route('/homepage')
def homepage():
    text = 'Welcome to Yummly Cuisine Prediction API, Redirecting in 3 seconds ...'

    # # Directly return result to the website
    # return text


    # time.sleep(3)

    # print(text)
    # return redirect(url_for('predict'))
    # return redirect('/predict')
    return render_template('homepage.html', title="Homepage", text = text)


@app.route('/formtest')
def testing():
    form = InputForm()
    if form.validate_on_submit():
        id = form.data('ID')
        recipe = form.data['Recipe']
    return render_template('formtest.html', form=form)


@app.route('/predict')
def prediction():
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
    return render_template('prediction.html', title="Prediction", test=test, body=body)
