import joblib as j
import pandas as pd


model = j.load("models\\ham-or-spam_model.pkl")

def prediction(data, model=model):
    if isinstance(data, str):  
        df = pd.DataFrame({"text": [data]})  
    else:
        df = pd.DataFrame(data)  

    predict = model.predict(df)  
    return predict[0] 