# step 1 undump our model
import pickle
import numpy as np
from flask import Flask, render_template, request
#render_template to show the html file,according to the request

# create an instance of a app means object like in node
app = Flask(__name__)
model= pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict',methods=['GET','POST'])
def predict():
    temperature = float(request.form.get('temperature'))
    prediction = model.predict(np.array([[temperature]]))
    output= round(prediction[0],2)#rounding off
    print(output)
    return render_template("index.html",prediction_text=f'Total revenue generated will be Rs. {output}')



if __name__=='__main__':
    app.run(debug=True)
   
