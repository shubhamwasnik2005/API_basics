from flask import Flask, render_template, request, jsonify


# class defination in app 
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html',result=result)

# Getting data from postman
@app.route('/via_postman', methods=['POST']) 
def math_operation_via_postman():
#CHECKING IF THE METHOD OF REQEST IS POST OR NOT
    if (request.method=='POST'):
        #GETTING INPUT FORM THE USER
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])

        
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


# sending data though url
# to test add app route and then ?val1=10&val2=20
@app.route('/url_test')
def url_test1():
    test1 = int(request.args.get('val1'))
    test2 = int(request.args.get('val2'))

    return '''result is {}'''.format(test1+test2)

if __name__ == '__main__':
    app.run()
