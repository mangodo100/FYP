from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model1 = pickle.load(open('model1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

standard_to = StandardScaler()
@app.route("/test", methods=['POST'])
def predict():
    if request.method == 'POST':
        Type=request.form['1']
        if(Type=='Medium'):
            value1=1
            value2=0
        elif(Type=='Slim'):
            value1=0
            value2=1
        else:
            value1=0
            value2=0 

        Type=request.form['2']
        if(Type=='moderate, no difficulties in gaining or loosing weight'):
            value3=1
            value4=0
        elif(Type=='heavy, difficulties in loosing weight'):
            value3=0
            value4=1
        else:
            value3=0
            value4=0 

        Type=request.form['3']
        if(Type=='Tall or short'):
            value5=1
            value6=0
        elif(Type=='Thin & sturdy / short & stocky'):
            value5=0
            value6=1
        else:
            value5=0
            value6=0

        Type=request.form['4']
        if(Type=='Light, small bones, 1rominent joints'):
            value7=1
            value8=0
        elif(Type=='Medium bone structure'):
            value7=0
            value8=1
        else:
            value7=0
            value8=0

        Type=request.form['5']
        if(Type=='Fair skin, sun burns easily'):
            value9=1
            value10=0
        elif(Type=='White, pale, tans evenly'):
            value9=0
            value10=1
        else:
            value9=0
            value10=0

        Type=request.form['6']
        if(Type=='thick and moist/greasy, cold'):
            value11=1
            value12=0
        elif(Type=='Smooth and warm, Oily T-zone'):
            value11=0
            value12=1
        else:
            value11=0
            value12=0

        Type=request.form['7']
        if(Type=='Freckles, many moles, redness, rashes and acne'):
            value13=1
            value14=0
        elif(Type=='Soft, glowing and youthful'):
            value13=0
            value14=1
        else:
            value13=0
            value14=0
    
        Type=request.form['8']
        if(Type=='Dull, black, brown'):
            value15=1
            value16=0
        elif(Type=='Red, light brown, yellow'):
            value15=0
            value16=1
        else:
            value15=0
            value16=0

        Type=request.form['9']
        if(Type=='Straight, Oily'):
            value17=1
            value18=0
        elif(Type=='Thick, Curly'):
            value17=0
            value18=1
        else:
            value17=0
            value18=0
        
        Type=request.form['10']
        if(Type=='Large, round, Full'):
            value19=1
            value20=0
        elif(Type=='Long, angular,Thin'):
            value19=0
            value20=1
        else:
            value19=0
            value20=0

        Type=request.form['11']
        if(Type=='Medium sized, penetrating, light sensetivity eyes'):
            value21=1
            value22=0
        elif(Type=='Small, active, darting, dark eyes'):
            value21=0
            value22=1
        else:
            value21=0
            value22=0

        Type=request.form['12']
        if(Type=='Scanty eye lashes'):
            value23=1
            value24=0
        elif(Type=='Thick/ Fused eye lashes'):
            value23=0
            value24=1
        else:
            value23=0
            value24=0
        
        Type=request.form['13']
        if(Type=='Moderate Blinking'):
            value25=1
            value26=0
        elif(Type=='More or less stable'):
            value25=0
            value26=1
        else:
            value25=0
            value26=0

        Type=request.form['14']
        if(Type=='Smooth, Flat'):
            value27=1
            value28=0
        elif(Type=='Wrinkled, Sunken'):
            value27=0
            value28=1
        else:
            value27=0
            value28=0

        Type=request.form['15']
        if(Type=='Crooked, Narrow, small'):
            value29=1
            value30=0
        elif(Type=='Rounded, Large open nostrils'):
            value29=0
            value30=1
        else:
            value29=0
            value30=0

        Type=request.form['16']
        if(Type=='Irregular, Protruding teeth, Receding gums'):
            value31=1
            value32=0
        elif(Type=='Medium sized teeth, Reddish gums'):
            value31=0
            value32=1
        else:
            value31=0
            value32=0
        
        Type=request.form['17']
        if(Type=='Lips are soft, medium-sized'):
            value33=1
            value34=0
        elif(Type=='Tight, thin, dry lips which chaps easily'):
            value33=0
            value34=1
        else:
            value33=0
            value34=0

        Type=request.form['18']
        if(Type=='Sharp, Flexible, pink, Lustrous'):
            value35=1
            value36=0
        elif(Type=='Thick, Oily, Smooth, Polished'):
            value35=0
            value36=1
        else:
            value35=0
            value36=0

        Type=request.form['19']
        if(Type=='Slow but steady'):
            value37=1
            value38=0
        elif(Type=='Strong, Unbearable'):
            value37=0
            value38=1
        else:
            value37=0
            value38=0

        Type=request.form['20']
        if(Type=='Sweet / Bitter / Astringent'):
            value39=1
            value40=0
        elif(Type=='Sweet / Sour / Salty'):
            value39=0
            value40=1
        else:
            value39=0
            value40=0

        output=model1.predict([[value1,value2,value3,value4,value5,value6,value7,value8,value9,value10,value11,value12,value13,value14,value15,value16,value17,value18,value19,value20,value21,value22,value23,value24,value25,value26,value27,value28,value29,value30,value31,value32,value33,value34,value35,value36,value37,value38,value39,value40]])
        # output=round(prediction[0],2)
        if output==0:
            return render_template('test.html',prediction_text="Prakruti Type : VATT".format(output))
        elif output==1:
            return render_template('test.html',prediction_text="Prakruti Type : PITT".format(output))
        elif output==2:
            return render_template('test.html',prediction_text="Prakruti Type : KAFF".format(output))
        elif output==3:
            return render_template('test.html',prediction_text="Prakruti Type : VATT-PITT".format(output))
        elif output==4:
            return render_template('test.html',prediction_text="Prakruti Type : VATT-KAFF".format(output))
        elif output==5:
            return render_template('test.html',prediction_text="Prakruti Type : PITT-KAFF".format(output))
    else:
        return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)

