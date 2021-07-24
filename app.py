from flask import Flask, render_template, request
import utils
app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html')

@app.route('/predict/', methods=['GET', 'POST']) 
def predict(): 
    if request.method == 'POST': 
        Glucose = request.form.get('Glucose')
        print(Glucose)
        Insulin = request.form.get('Insulin')
     
        print(Insulin)
        

    prediction = utils.preprocessdata(Glucose,Insulin) 

    return render_template('predict.html', prediction=prediction) 
if __name__ == '__main__': 
    app.run(debug=True)