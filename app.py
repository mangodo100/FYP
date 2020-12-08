from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    # data1 = request.form['1']
    # data2 = request.form['2']
    # data3 = request.form['3']
    # data4 = request.form['4']
    # data5 = request.form['5']
    # data6 = request.form['6']
    # data7 = request.form['7']
    # data8 = request.form['8']
    # data9 = request.form['9']
    # data10 = request.form['10']
    # data11 = request.form['11']
    # data12 = request.form['12']
    # data13 = request.form['13']
    # data14 = request.form['14']
    # data15 = request.form['15']
    # data16 = request.form['16']
    # data17 = request.form['17']
    # data18 = request.form['18']
    # data19 = request.form['19']
    # data20 = request.form['20']

    # arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,2]])
    # pred = model.predict(arr)
    # return render_template('after.html', data=pred)

    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    pred=model.predict(final)

    if pred == 0:
        return render_template('home.html', pred='VATT')

    if pred == 1:
        return render_template('home.html', pred='PITT')

    if pred == 2:
        return render_template('home.html', pred='KAFF')

    if pred == 3:
        return render_template('home.html', pred='VATT-PITT')

    if pred == 4:
        return render_template('home.html', pred='PITT-KAFF')

    if pred == 5:
        return render_template('home.html', pred='VATT-KAFF')


if __name__ == "__main__":
    app.run(debug=True)