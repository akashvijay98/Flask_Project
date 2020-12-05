from flask import Flask,render_template,request,make_response
app = Flask(__name__)


@app.route('/')

def index():
	return render_template('ind.html')

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
	if request.method=='POST':
		user=request.form['nm']
		resp=make_response(render_template('readcookie.html'))
		resp.set_cookie('userid',user)

	return resp


@app.route('/getcookie')
def getcookie():
	name=request.cookies.get('userid')
	return '<h1> Welome'+ name + '<h1>'



app.run(host='0.0.0.0', port=3000,debug=True)
