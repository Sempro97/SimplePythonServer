import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/<article>')
def hello(article=None):
    return render_template('index.html', article=article)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=os.getenv('PORT'))