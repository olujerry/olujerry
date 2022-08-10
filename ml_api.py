# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 02:46:34 2022

@author: Jeremiah
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
     
    ID : int
    Age : float
    Hypertension : int
    HeartDisease : int
    AverageGlucoseLevel : float
    BMI : float

stroke_model = pickle.load(open('stroke_model.sav','rb'))

@app.post('/stroke_prediction') 
def stroke_pred(input_parameters: model_input):
    
    input_data= input_parameters.json()
    input_dictionary = json.loads(input_data)  
    
    ID = input_dictionary['ID']
    age = input_dictionary['Age']
    hyp = input_dictionary['Hypertension']
    heart=input_dictionary['HeartDisease']
    avg= input_dictionary['AverageGlucoseLevel']
    bmi=input_dictionary['BMI']
    
     input_list = [ID, age, hyp, heart, avg, bmi]
    
    prediction =stroke_model.predict([input_list])
    
    if  (prediction[0]== 0):
        return'The Person does not have stroke'
    else:
        return'The Person has stroke'