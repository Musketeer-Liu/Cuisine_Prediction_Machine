import flask
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)



__author__ = "Musketeer Liu"


import time, json, subprocess, re, urllib

from flask import redirect, render_template, url_for, request, Response

from application import app
from application.forms import InputForm
from application.pipeline import *
from config import *



cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    def inner():
        proc = subprocess.Popen(
            ['dmesg'],             #call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(1)                           # Don't need this just shows the text streaming
            yield line.rstrip() + '<br/>\n'

    return Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$


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




# Need int() otherwise it will be a float
BASE = int(1e5)


@app.route('/predict', methods=['POST'])
def result():


    #return jsonify(results)

    # requests package
    # request from flask

    RESULT = []
    # data_bits = request.get_data()
    # print('Data in Bits: ', data_bits)
    # # data_bits:  b'csrf_token=IjQwMjcyZGNhNjUxZTE0ODM4NGI0MWZmMjlmYTlkMDVjZGY3YzE3MTEi.XrJhgg.e01etQ0lhsQ2UpMunExN_XDnb_k&id=1&ingredients=beef%2C+tomato&submit=Predict'
    # decode_list = data_bits.decode('ascii').split('&')
    # # decode_list:['csrf_token=IjQwMjcyZGNhNjUxZTE0ODM4NGI0MWZmMjlmYTlkMDVjZGY3YzE3MTEi.XrJhgg.e01etQ0lhsQ2UpMunExN_XDnb_k', 'id=1', 'ingredients=beef+tomato', 'submit=Predict']
    # id = int(decode_list[1].split('=')[1])
    # recipes = decode_list[2].split('=')[1].split('%2C')
    id = request.args['id']
    recipes = request.args['recipes']

    print('id: ',id,'\nrecipes: ',recipes)

    recipes = recipes.split(",")
    print('after removing commas ',recipes)
    ingredients = []
    for recipe in recipes:
        # ingredients += [recipe.replace('+', ' ').strip().lower()]
        ingredients.append(recipe.lower().strip())
    print('Ingredients: ', ingredients)

    data_dict = dict()
    # Add BASE to id to avoid mess up w, we can also delete id input form
    data_dict['id'] = int(id) + BASE
    data_dict['ingredients'] = ingredients
    print(json.dumps(data_dict, sort_keys=True, indent=4))


    print('Data in Dict: ', data_dict['ingredients'])
    ingredients = data_dict['ingredients']

    if Config.FLASK_ENV == 'development':
        ingredient_dataset = pd.read_csv('dataset_developing.csv', header=0, nrows=1)
    else:
        ingredient_dataset = pd.read_csv('dataset_production.csv', header=0, nrows=1)

    print('Dataset Header: ', ingredient_dataset.columns[3:])

    index, width = ingredient_dataset.shape
    print('Row Count: {} | Col Count: {}'.format(index, width))


    row_request = pd.DataFrame(data=np.zeros((1, width), dtype=int), columns=ingredient_dataset.columns)
    print('Empty Row for Client Request: ', row_request)

    for ingredient in ingredient_dataset.columns[3:]:
        if ingredient in ingredients:
            row_request.loc[0, ingredient] = 1
        else:
            row_request.loc[0, ingredient] = 0
    print('Filled Row for Client Request: ', row_request)


    X_request = row_request[row_request.columns[3:]]
    print('Processed Features from Client Request: \n', X_request)


    predict_request = model_log.predict(X_request)
    probability = model_log.predict_proba(X_request)
    print('Cuisine Predicted: {} corresponding Probalibilty: {}'.format(predict_request, probability))


    row_request[row_request.columns[1]] = data_dict['id']
    row_request[row_request.columns[2]] = predict_request[0]
    print('Client Request with Predicted Cuisine: \n', row_request)


    result = dict()
    result['id'] = data_dict['id'] - BASE
    result['ingredients'] = data_dict['ingredients']
    result['cuisine'] = predict_request[0]
    result['probability'] = round(max(probability[0]), 4)

    RESULT.append(result)

    print('Pipeline Done!')
    data = {"results":RESULT}
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

