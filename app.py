import smtpd
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.metrics import accuracy_score
import sklearn
from scipy.io import arff
app = Flask(__name__)


dir_path = os.path.dirname(os.path.realpath(__file__))
model = pickle.load(open(dir_path + '\\model.pkl', 'rb'))

from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
columns =  ["net_profit","total_liabilities","profit_operating_activities","profit_on_sales","sales_minus_cost"]
columns_to_keep = ["Attr1","Attr2","Attr27","Attr35","Attr56"]
import os
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]

    df = pd.DataFrame(columns= columns)
    df.loc[0] = float_features

    prediction = model.predict(df)

    output = round(prediction[0], 2)
    if(output == 0):
        return render_template('index.html', prediction_text='Youre not going to bankrupt'.format(output))
    else :
        return render_template('index.html', prediction_text='Youre going right to bankrupt'.format(output))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)




@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    array_pred = []
    if request.method == 'POST':
        upload_file = request.files['file']
        if upload_file.filename != '':
            file_path = os.path.join(os.getcwd(),upload_file.filename)
            upload_file.save(file_path)
            data = arff.loadarff(file_path)
            df = pd.DataFrame(data[0])
            X = df.drop(['class'], axis=1)
            Y = df['class'].to_numpy()
            Y = Y.astype(int)

            for i in X.index:
                float_features = []
                for y in columns_to_keep:
                    float_features.append(X[y][i])
                df = pd.DataFrame(columns=columns)
                df.loc[0] = float_features
                prediction = model.predict(df)

                output = round(prediction[0], 2)
                array_pred.append(output)
            return (f"Pour votre dataset , l'accuracy est de {accuracy_score(Y,array_pred)}")



if __name__ == "__main__":
    app.run(debug=True)
