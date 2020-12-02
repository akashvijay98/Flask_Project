@app.route('/',methods=['GET','POST'])
def signUp():
 
    # read the posted values from the UI
    if request.form:
    	conn = mysql.connect()
    	cursor = conn.cursor()
    	_name = request.form['ipname']
    	_email = request.form['eid']
    	_password = request.form['psd']

    	cursor.execute('INSERT INTO Users VALUES(%s,%s,%s)',(_name,_email,_password,))  #can either use stored procedures or the cursor execute command.
    	
    	data = cursor.fetchall()
    	if len(data) is 0:
    		conn.commit()
    		return json.dumps({'message':'User created successfully !'})
    	else:
    		return json.dumps({'error':str(data[0])})



    	print(_name,_email)
 
    # validate the received values
    	if _name and _email and _password:
        	return json.dumps({'html':'<span>All fields good  !!</span>'})
    	else:
        	return json.dumps({'html':'<span>Enter the required fields</span>'})

    return render_template('signup.html')
	
	
 
	


app.run(host='0.0.0.0', port=8000,debug=True)
