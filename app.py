import numpy as np
from flask import Flask, request,jsonify,render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('taxi.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features =[int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    return render_template('index.html',prediction_text="Number of weekly rides should be {}".format(math.floor(output)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
