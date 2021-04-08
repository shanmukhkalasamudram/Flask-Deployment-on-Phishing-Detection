import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    

    a = request.form['numbe']
    b = request.form['ip']
    c = request.form['lurl']
    d = request.form['surl']
    e = request.form['symbol']
    f = request.form['redirecting']    
    g = request.form['pre']
    h = request.form['sd']
    i = request.form['https']
    j = request.form['len']
    k  = request.form['fav']
    l = request.form['port']
    m = request.form['hturl']
    n = request.form['rurl']
    o = request.form['aurl']
    aa = request.form['link']
    ab = request.form['server']
    ac = request.form['Email']
    ad = request.form['aurl']
    ae = request.form['forward']
    af = request.form['status']
    ag = request.form['right']
    ah = request.form['pop']
    aq = request.form['ir']
    ba = request.form['age']
    bb = request.form['dns']
    bc = request.form['wt']
    bd = request.form['pr']
    be = request.form['gi']
    bf = request.form['point']
    bh = request.form['stat']



 

    arr = np.array([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,aa,ab,ac,ad,ae,ag,ah,aq,ba,bb,bc,bd,be,bf,bh]])
   
    pred = model.predict(arr)

    if(pred == -1):
        text = "This is safe Website"

    else:
        text = "This is phishing Website"

    return render_template('index.html', prediction_text=text)



if __name__ == "__main__":
    app.run(debug=True)