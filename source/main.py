import os
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=os.getenv('PORT'))