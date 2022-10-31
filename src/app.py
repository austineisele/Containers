from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')



if __name__ == "__main__":
    app.run(host="0.0.0.0")