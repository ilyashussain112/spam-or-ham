import joblib as j
import pandas as pd


model = j.load("models/ham-or-spam.pkl")
tfidf = j.load("models/tfidf.pkl")

def prediction(data, model=model, tfidf=tfidf):
    if (data, str):  
        df = pd.DataFrame({"text": [data]})  
    else:
        df = pd.DataFrame(data)  
        
    transformed_data = tfidf.transform(df["text"])  


    predict = model.predict(transformed_data)  
    prediction_label = "Spam" if predict[0][0] > 0.5 else "Ham"

    return prediction_label