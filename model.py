from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


app = Flask(__name__)

with open('classifier.pkl', 'rb') as clf:
    classifier = pickle.load(clf)
        
def preprocess(txt):
    ''' Transorms the input as per the requirement of the model'''
     
    input_file = pd.read_csv(txt, header=None)  
    input_file = input_file.replace('na', np.NaN)                
    
    
    with open('Discard_Features.pkl', 'rb') as df:
        discard_features = pickle.load(df)
    input_file = input_file.drop(discard_features, axis =1)
    
    with open('Imputer.pkl', 'rb') as imp:
        knn_imp = pickle.load(imp)
    test_imp = knn_imp.transform(input_file)
    
    with open('standardizer.pkl', 'rb') as scale:
        std = pickle.load(scale)
    test_std = std.transform(test_imp)
    
    with open('PCA_features.pkl', 'rb') as fe:
        pca = pickle.load(fe)
    test_80 = pca.transform(test_std)
    
    return test_80




@app.route('/')
def man():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    vehicle = request.files['file']
    instance = preprocess(vehicle)
    pred = classifier.predict(instance)
    return render_template('result.html', data=pred)
if __name__ == "__main__":
    app.run(debug=True)

