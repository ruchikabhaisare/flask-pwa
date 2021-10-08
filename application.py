from flask import Flask, redirect,render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')


if __name__=='__main__':
    application.run(host="0.0.0.0", port=8000, debug=True)
