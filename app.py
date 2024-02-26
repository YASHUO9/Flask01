from flask import Flask,render_template

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

@app.route("/calculate")
def calculate():
    return render_template("calculate.html")

# def calculateMarks():
#     retturn ""


if __name__ == "__main__":
    app.run(debug=True)