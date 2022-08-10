# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:18:41 2022

@author: ienovo
"""

import json
import requests

url='http://127.0.0.1:8000/stroke_prediction'

input_data_for_model = {
   
    "ID" : 9046,
    "Age" : 67.0,
    "Hypertension" : 0,
    "HeartDisease" : 1,
    "AverageGlucoseLevel" : 228.69,
    "BMI" : 36.6
    
    }
    
   

input_json =json.dumps(input_data_for_model)

response = requests.post(url,data=input_json)

print(response.text)