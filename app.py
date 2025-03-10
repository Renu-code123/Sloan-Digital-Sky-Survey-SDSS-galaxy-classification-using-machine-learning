from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from form
        features = [float(x) for x in request.form.values()]
        input_data = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(input_data)
        
        return render_template('output.html', prediction=prediction[0])

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
