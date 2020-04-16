
	
from flask import Flask, render_template,request
app = Flask(__name__)
 
@app.route("/")
def hello():
	return render_template('inputs.html')
	
@app.route("/results", methods=['GET', 'POST'])
def results():
    num1= (request.form['num1'])
    num2=(request.form['num2'])
    print(num1)
    print(num2)
    sum = num1 + num2
    return sum
	

 
if __name__ == "__main__":
	app.run()