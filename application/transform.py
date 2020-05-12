__author__ = "Musketeer Liu"




#Import Libraries
import pandas as pd
import numpy as np


from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split


import os, json, time
from pathlib import Path


from config import *
from utility import *


INGREDIENT_MENU = []
FILE = './cuisine.train.v2.json'


## Transform Module
def generate_ingredient_menu():
    global INGREDIENT_MENU

    file = './cuisine.train.v2.json'

    with open(file, 'r', encoding='UTF-8') as f:
        cuisines = json.load(f)


    ingredients_set = set()
    for cuisine in cuisines:
        ingredients = set(cuisine['ingredients'])
        ingredients_set = ingredients_set | ingredients

    ingredients_list = list(ingredients_set)
    print(len(ingredients_list))
    INGREDIENT_MENU = ingredients_list
    return ingredients_list



# Transform JSON File to Production CSV Form
def json_to_csv_production(file):
    print('Begin JSON file transfrom to CSV Form...')
    file = './cuisine.train.v2.json'

    with open(file, 'r', encoding='UTF-8') as f:
        cuisines = json.load(f)


    ingredients_set = set()
    for cuisine in cuisines:
        ingredients = set(cuisine['ingredients'])
        ingredients_set = ingredients_set | ingredients

    ingredients_list = list(ingredients_set)
    print("Production Ingredients Menu Length:", len(ingredients_list))
    INGREDIENT_MENU = ingredients_list
    print(Fore.BLUE + "Ingredient Menu:" + Fore.RESET)
    print(INGREDIENT_MENU)
    print('\n')


    dataset = pd.DataFrame(columns=['id', 'cuisine']+ingredients_list)


    data_template = np.zeros([len(cuisines), len(ingredients_list)+2])
    dataset = pd.DataFrame(data = data_template, columns=['id', 'cuisine']+ingredients_list)


    print(Fore.BLUE + 'Transforming JSON data into CSV ...' + Fore.RESET)
    for index, cuisine in enumerate(cuisines):
        print('Processing Line: ', index)

        dataset.loc[index, 'id'] = cuisine['id']
        dataset.loc[index, 'cuisine'] = cuisine['cuisine']

        ingredients = cuisine['ingredients']
        for column in ingredients:
            dataset.loc[index, column] = 1


    dataset.to_csv('dataset_production.csv')
    print('Complete JSON file transfrom to Production CSV Form, {} lines data in total'.format(index))


# Transform JSON File to Developing CSV Form
def json_to_csv_developing(file):
    global INGREDIENT_MENU

    print(Fore.GREEN + 'Begin JSON file transfrom to Developing CSV Form... \n' + Fore.RESET)
    file = './cuisine.train.v2.json'

    with open(file, 'r', encoding='UTF-8') as f:
        cuisines = json.load(f)[:401]

    ingredients_set = set()
    for cuisine in cuisines:
        ingredients = set(cuisine['ingredients'])
        ingredients_set = ingredients_set | ingredients

    ingredients_list = list(ingredients_set)
    INGREDIENT_MENU = ingredients_list
    print("Production Ingredients Menu Length:", len(ingredients_list))
    print(Fore.BLUE + "Ingredient Menu:" + Fore.RESET)
    print(INGREDIENT_MENU)
    print('\n')


    dataset = pd.DataFrame(columns=['id', 'cuisine']+ingredients_list)



    data_template = np.zeros([len(cuisines), len(ingredients_list)+2])
    dataset = pd.DataFrame(data = data_template, columns=['id', 'cuisine']+ingredients_list)


    print(Fore.BLUE + 'Transforming JSON data into CSV ...' + Fore.RESET)
    for index, cuisine in enumerate(cuisines):
        print('Processing Line: ', index)

        dataset.loc[index, 'id'] = cuisine['id']
        dataset.loc[index, 'cuisine'] = cuisine['cuisine']

        ingredients = cuisine['ingredients']
        for column in ingredients:
            dataset.loc[index, column] = 1


    dataset.to_csv('dataset_developing.csv')
    print(Fore.GREEN + 'Complete JSON file transfrom to Developing CSV Form, {} lines data in total'.format(index) + Fore.RESET)




# Denote Features and Label
def preprocess_dataset(dataset):
    feature_selected = dataset.columns[3:]
    label_selected = dataset.columns[2]
    return dataset[feature_selected], dataset[label_selected]




# #  Encode Label (Cuisine Names) into Numbers
# def preprocess_dataset(label_selected):
    # cuisine_to_id = dict()
    # id_to_cuisine = dict()
    # for index, label in enumerate(list(set(label_selected))):
    #     if label not in cuisine_to_id:
    #         cuisine_to_id[label] = index
    #         id_to_cuisine[index] = label

    # label_processed = label_selected[:]
    # for i, label in enumerate(label_selected):
    #     label_processed[label] = index

    # return label_processed




# Result Presentation
def result_presentation(truevalue, prediction):
    compare, correct = [], 0
    for a, b in zip(truevalue, prediction):
        compare += [(a, b)]
        if a == b: correct += 1
    return compare, correct
