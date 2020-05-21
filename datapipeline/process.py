__author__ = 'Musketeer Liu'


import json


from datapipeline.pipeline import *
from config import *




# Need int() otherwise it will be a float
BASE = int(1e5)




def request_prediction_flask(data_bits):
    print('Data in Bits: ', data_bits)
    # data_bits:  b'csrf_token=IjQwMjcyZGNhNjUxZTE0ODM4NGI0MWZmMjlmYTlkMDVjZGY3YzE3MTEi.XrJhgg.e01etQ0lhsQ2UpMunExN_XDnb_k&id=1&ingredients=beef%2C+tomato&submit=Predict'
    decode_list = data_bits.decode('ascii').split('&')
    # decode_list:['csrf_token=IjQwMjcyZGNhNjUxZTE0ODM4NGI0MWZmMjlmYTlkMDVjZGY3YzE3MTEi.XrJhgg.e01etQ0lhsQ2UpMunExN_XDnb_k', 'id=1', 'ingredients=beef+tomato', 'submit=Predict']
    id = int(decode_list[1].split('=')[1])
    recipes = decode_list[2].split('=')[1].split('%2C')

    ingredients = []
    for recipe in recipes:
        # ingredients += [recipe.replace('+', ' ').strip().lower()]
        ingredients.append(recipe.replace('+', ' ').strip().lower())
    print('Ingredients: ', ingredients)

    data_dict = dict()
    # Add BASE to id to avoid mess up w, we can also delete id input form
    data_dict['id'] = id + BASE
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


    results = dict()
    results['id'] = data_dict['id'] - BASE
    results['ingredients'] = data_dict['ingredients']
    results['cuisine'] = predict_request[0]
    results['probability'] = round(max(probability[0]), 4)

    return results




def request_prediction_react(id, recipes):
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


    prediction = dict()
    prediction['id'] = data_dict['id'] - BASE
    prediction['ingredients'] = data_dict['ingredients']
    prediction['cuisine'] = predict_request[0]
    prediction['probability'] = round(max(probability[0]), 4)

    return prediction



