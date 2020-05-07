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


INGREDIENT_LIST = []



## Utilities Module
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
    print(len(ingredients_list))
    INGREDIENT_LIST = ingredients_list


    dataset = pd.DataFrame(columns=['id', 'cuisine']+ingredients_list)


    data_template = np.zeros([len(cuisines), len(ingredients_list)+2])
    dataset = pd.DataFrame(data = data_template, columns=['id', 'cuisine']+ingredients_list)

    for index, cuisine in enumerate(cuisines):
        print('Processing Line: ', index)

        dataset.loc[index, 'id'] = cuisine['id']
        dataset.loc[index, 'cuisine'] = cuisine['cuisine']

        ingredients = cuisine['ingredients']
        for column in ingredients:
            dataset.loc[index, column] = 1


    dataset.to_csv('dataset_developing.csv')
    print(Fore.GREEN + 'Complete JSON file transfrom to Production CSV Form, {} lines data in total'.format(index))


# Transform JSON File to Developing CSV Form
def json_to_csv_developing(file):
    print(Fore.GREEN + 'Begin JSON file transfrom to Developing CSV Form...')
    file = './cuisine.train.v2.json'

    with open(file, 'r', encoding='UTF-8') as f:
        cuisines = json.load(f)[:401]

    ingredients_set = set()
    for cuisine in cuisines:
        ingredients = set(cuisine['ingredients'])
        ingredients_set = ingredients_set | ingredients

    ingredients_list = list(ingredients_set)
    INGREDIENT_LIST = ingredients_list
    print(INGREDIENT_LIST)


    dataset = pd.DataFrame(columns=['id', 'cuisine']+ingredients_list)



    data_template = np.zeros([len(cuisines), len(ingredients_list)+2])
    dataset = pd.DataFrame(data = data_template, columns=['id', 'cuisine']+ingredients_list)

    for index, cuisine in enumerate(cuisines):
        print('Processing Line: ', index)

        dataset.loc[index, 'id'] = cuisine['id']
        dataset.loc[index, 'cuisine'] = cuisine['cuisine']

        ingredients = cuisine['ingredients']
        for column in ingredients:
            dataset.loc[index, column] = 1


    dataset.to_csv('dataset_developing.csv')
    print(Fore.GREEN + 'Complete JSON file transfrom to Developing CSV Form, {} lines data in total'.format(index))




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








## Pipeline Module
# Check source data
print(Fore.RED + 'Pipeline Initiation ...')
print('\n')

print('Checking if source csv data is in current folder ==> ', end="")
source_json = Path("./cuisine.train.v2.json")
source_csv_production = Path("./dataset_production.csv")
source_csv_developing = Path("./dataset_developing.csv")




if not source_json.is_file():
    print("Please ask for Original JSON Data and run this file again.")
    print("Program will close in 5 seconds ...")
    time.sleep(5)
    os._exit()

if Config.TESTING:
    if not source_csv_developing.is_file():
        print(Fore.GREEN + "Tranform JSON Data to CSV Data Developing ==> ", end="")
        json_to_csv_developing(source_json)
else:
    if not source_csv_production.is_file():
        print("Tranform JSON Data to CSV Data Production ==> ", end="")
        json_to_csv_production(source_json)
print('We have CSV Data!')
print('\n')




# # Load Smaller Dataset for faster Debugging into 3 Parts ((Train-Valid)-Final)
# print('Working on Smaller Dataset for Quick Debugging: ')
# print('Loading Train Dataset ==> ', end="")
# dataset_train = pd.read_csv('dataset_production.csv', header=0, nrows=300, low_memory=False)
# print('Loaded! ==> ', end="")

# print('Loading Valid Dataset ==> ', end="")
# dataset_valid = pd.read_csv('dataset_production.csv', header=0, skiprows=300, nrows=90)
# print('Loaded! ==> ', end="")

# print('Loading Final Dataset ==> ', end="")
# dataset_final = pd.read_csv('dataset_production.csv', header=0, skiprows=390, nrows=10)
# print('Loaded!')


# Load Smaller Dataset for Test Prediction into 3 Parts ((Train-Valid)-Final)
if Config.TESTING:
    print(Fore.GREEN + 'Working on Small Dataset for Test Prediction: ')
    print('Loading Train Dataset ==> ', end="")
    dataset_train = pd.read_csv('dataset_developing.csv', header=0, nrows=300, low_memory=False)
    print('Loaded! ==> ', end="")

    print('Loading Valid Dataset ==> ', end="")
    dataset_valid = pd.read_csv('dataset_developing.csv', header=0, skiprows=300, nrows=90)
    print('Loaded! ==> ', end="")

    print('Loading Final Dataset ==> ', end="")
    dataset_final = pd.read_csv('dataset_developing.csv', header=0, skiprows=390, nrows=10)
    print('Loaded!')


# Load Whole Dataset for Real Prediction into 3 Parts ((Train-Valid)-Final)
else:
    print('Working on Whole Dataset for Real Prediction: ')
    print('Loading Train Dataset ==> ', end="")
    dataset_train = pd.read_csv('dataset_production.csv', header=0, nrows=30000, low_memory=False)
    print('Loaded! ==> ', end="")

    print('Loading Valid Dataset ==> ', end="")
    dataset_valid = pd.read_csv('dataset_production.csv', header=0, skiprows=30000, nrows=9000)
    print('Loaded! ==> ', end="")

    print('Loading Final Dataset ==> ', end="")
    dataset_final = pd.read_csv('dataset_production.csv', header=0, skiprows=39000)
    print('Loaded!')


# print('Saving Final Label... ')
# feature_final = dataset_final.columns
# print(feature_final)
# feature_final.to_csv('feature_final.csv')
# print('Saved Final Label!')
print('\n')




# Denote Features and Label
print(Fore.RED + 'Denote Features and Label ==> ', end="")
X_train, y_train = preprocess_dataset(dataset_train)
X_valid, y_valid = preprocess_dataset(dataset_valid)
X_final, y_final = preprocess_dataset(dataset_final)
print('Features and Label Denoted!')
print('\n')




# Create Navie Bayes Model object
print('Model Initiation ==> ', end="")
model_log = LogisticRegression()
# model_rfc = RandomForestClassifier(n_estimators=200)
model_rfc = RandomForestClassifier()
model_bnb = BernoulliNB()


# Train model on training dataset
print('Model Training ==> ', end="")
model_log.fit(X_train, y_train)
model_rfc.fit(X_train, y_train)
model_bnb.fit(X_train, y_train)


# Check Model Score
print('Logistic Regression Model Score: {:.4f}'.format(model_log.score(X_valid, y_valid)), end="  ||  ")
print('Random Forest Model Log Probability: {:.4f}'.format(model_rfc.score(X_valid,y_valid)), end="  ||  ")
print('Bernoullli Naive Bayes Model Score: {:.4f}'.format(model_bnb.score(X_valid, y_valid)))
print('\n')


# # Check Detailed Model Info
# print('Predict_Probability: \n', model_bnb.predict_proba)




# Print out Model Alignment/Prediction
# # Tuning Model with Valide Dataset
# print('Model Alignment with Valid Dataset ==> ', end="")
# predict_log = model_log.predict(X_valid)
# predict_rfc = model_rfc.predict(X_valid)
# predict_bnb = model_bnb.predict(X_valid)
# true_value = y_valid.tolist()
# print('Alignment Finished!')
# print('\n')


# Last Prediction with Final Dataset
print('Model Prediction on Final Dataset ==> ', end="")
predict_log = model_log.predict(X_final)
predict_rfc = model_rfc.predict(X_final)
predict_bnb = model_bnb.predict(X_final)
true_value = y_final.tolist()
print('Prediction Finished!')
print('\n')



# Compare Logistic Regression Model with Real Data
print('Compare Logistic Regression Prediction with True Value -- (True Value, Prediction): ')
compare_log, correct_log = result_presentation(true_value, predict_log)
print('Logistic Regression Corrected Rate = {:.4f}'.format(correct_log/len(compare_log)))
print('\n')
print(compare_log)
print('\n')


# Compare Random Forest Model with Real Data
print('Compare Random Forest Prediction with True Value -- (True Value, Prediction): ')
compare_rfc, correct_rfc = result_presentation(true_value, predict_rfc)
print('Random Forest Classifer Corrected Rate = {:.4f}'.format(correct_rfc/len(compare_rfc)))
print('\n')
print(compare_rfc)
print('\n')


# Compare Bernoulli Naive Bayes Model with Real Data
print('Compare Bernoulli Naive Bayes Prediction with True Value -- (True Value, Prediction): ')
compare_bnb, correct_bnb = result_presentation(true_value, predict_bnb)
print('Bernoulli Naive Bayes Corrected Rate = {:.4f}'.format(correct_bnb/len(compare_bnb)))
print('\n')
print(compare_bnb)
print('\n')


print('Pipeline Completed!')
print('\n')




if __name__ == '__main__':
    pass

