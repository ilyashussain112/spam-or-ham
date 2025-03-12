from flask import Flask, render_template, request
import pandas as pd
from predict import prediction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == "POST":
        user_input = str(request.form["user_text"])
        result = prediction(user_input) 
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000",debug=True)
