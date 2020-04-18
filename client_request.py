__author__ = "Yutong Liu"




import urllib
import requests
import json




URL  = "http://127.0.0.1"
PORT = "5000"
API  = "predict"




def request_example():
    url = URL + ':' + PORT + '/' + API

    data_text_list = [
        {
            'id': 397784,
            'ingredients': ['beef brisket', 'sauce tamota', 'carrots', 'red onion', 'fine sea salt']
        },
        {
            'id': 123456,
            'ingredients': ['tvp', 'mutton', 'lemon cake mix', 'sauce tamota', 'jack cheese', 'fine sea salt']
        }
    ]


    data_dict_list = json.dumps(data_text_list)

    response = requests.post(url=url, data=data_dict_list)

    return response




if __name__ == '__main__':
    request_example()



