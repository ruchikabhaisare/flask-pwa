from flask import Flask, redirect,render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/service-worker.js')
def sw():
    return application.send_static_file('service-worker.js')


if __name__=='__main__':
    application.run(host="0.0.0.0", port=5000, debug=True)
