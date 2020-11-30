from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    _name = request.form['ipname']
    _email = request.form['eid']
    _password = request.form['psd']
 
    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


app.run(host='0.0.0.0', port=8000,debug=True)
