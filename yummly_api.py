__author__ = "Yutong Liu"




from flask import Flask, request, render_template, redirect, url_for
import json, time


from yummly_model import *




app = Flask(__name__)




RESULT = []


@app.route('/')
def homepage():
    text = 'Welcome to Yummly Cuisine Prediction API, Redirecting in 3 seconds ...'
    time.sleep(3)
    # return text
    print(text)
    # return redirect(url_for('predict'))
    return redirect('/predict')


@app.route('/predict', methods=['GET', 'POST'])
def prediction():
    global RESULT
    
    if request.method == 'POST':
        data_bits_list = request.get_data()
        print('Data List in Bits: ', data_bits_list)
        data_dict_list = json.loads(data_bits_list)
        for data_dict in data_dict_list:
            print('Data in Dict: ', data_dict['ingredients'])
            ingredients = data_dict['ingredients']

            ingredient_dataset = pd.read_csv('yummly_dataset.csv', header=0, nrows=1)
            print('Dataset Header: ', ingredient_dataset.columns[3:])
            
            index, width = ingredient_dataset.shape
            print('Row Count: {} | Col Count: {}'.format(index, width))
            # id = ingredient_dataset.count
            # print(id)

            row_request = pd.DataFrame(data=np.zeros((1, width), dtype=int), columns=ingredient_dataset.columns)
            print('Empty Row for Client Request: ', row_request)
                    
            for ingredient in ingredient_dataset.columns[3:]:
                if ingredient in ingredients:
                    row_request.loc[0, ingredient] = 1
                else:
                    row_request.loc[0, ingredient] = 0
            print('Filled Row for Client Request: ', row_request)
            

            # data_request = row_request.index[0]
            # print('Processed Features from Client Request: \n', data_request)
            X_request = row_request[row_request.columns[3:]]
            print('Processed Features from Client Request: \n', X_request)

            predict_request = model_log.predict(X_request)
            probability = model_log.predict_proba(X_request)
            print('Cuisine Predicted: {} corresponding Probalibilty: {}'.format(predict_request, probability))

            row_request[row_request.columns[1]] = data_dict['id']
            row_request[row_request.columns[2]] = predict_request[0]
            print('Client Request with Predicted Cuisine: \n', row_request)

            # ingredient_dataset.append(row_request)
            # print('Updated client request into the databset!')
            result = dict()
            result['id'] = data_dict['id']
            result['ingredients'] = data_dict['ingredients']
            result['cuisine'] = predict_request[0]
            result['probability'] = round(max(probability[0]), 4)

            RESULT.append(result)

        # result = ''
        # result += 'Received ingredients are: {} | '.format(str(data_bits))
        # result += 'Predicted Cuisine is: {}'.format(predict_request)
        # print(result)

        return 'Pipeline Done!'
        # return redirect(url_for('predict'), code=307)
        # return render_template('predict.html', result=result)


    else:
        if RESULT == []:
            info = ''
            info += 'Here is an example of valid request input: '
            info += """            
                [
                    {
                        'id': 397784,
                        'ingredients': ['beef brisket', 'sauce tamota', 'carrots', 'white onion', 'fine sea salt']
                    },
                    {
                        'id': 123456,
                        'ingredients': ['tvp', 'mutton', 'lemon cake mix', 'sauce tamota', 'jack cheese', 'fine sea salt']
                    }
                ]
            """
            return info
        else: 
            return render_template('predict.html', result=RESULT)
    



if __name__ == '__main__':
    app.run()



