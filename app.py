from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello, World!</h1>"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return "Welcome to the contact page!"   


@app.route("/blog/<int:score>")
def blog(score):
    return "Welcome to the blog page! And the score is: " + str(score)

@app.route("/calculate",methods=["GET","POST"])
def calculate():
    if request.method == 'GET':
        return render_template("calculate.html")
    else:
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))
        operation = request.form.get("operation")
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2
        else:
            result = "Invalid operation"
        return render_template('result.html',results =str(result))



if __name__ == "__main__":
    app.run(debug=True)