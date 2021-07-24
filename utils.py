import numpy as np 
import joblib 


def preprocessdata(Glucose,Insulin):
    test_data = [[Glucose,Insulin]] 
    trained_model = joblib.load("model.pkl") 

    prediction = trained_model.predict(test_data) 

    return prediction 
