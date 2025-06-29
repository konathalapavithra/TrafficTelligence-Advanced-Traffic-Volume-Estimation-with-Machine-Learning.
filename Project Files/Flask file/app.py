
from flask import Flask, render_template, request
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input from form
        features = [
            int(request.form['holiday']),
            float(request.form['temp']),
            float(request.form['rain']),
            float(request.form['snow']),
            int(request.form['weather']),
            int(request.form['year']),
            int(request.form['month']),
            int(request.form['day']),
            int(request.form['hours']),
            int(request.form['minutes']),
            int(request.form['seconds'])
        ]

        # Make prediction
        prediction = model.predict([features])
        result = int(prediction[0])

        return render_template('output.html', prediction_text=f"Estimated Traffic Volume is: {result} units") 

    except Exception as e:
        return render_template('output.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)