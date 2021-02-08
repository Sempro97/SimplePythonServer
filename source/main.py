import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/<article>')
def hello(article=None):
    url_for('static', filename='assets/img/favicon.png')
    url_for('static', filename='assets/img/apple-touch-icon.png')
    url_for('static', filename='assets/vendor/bootstrap/css/bootstrap.min.css')
    url_for('static', filename='assets/vendor/icofont/icofont.min.css')
    url_for('static', filename='assets/vendor/boxicons/css/boxicons.min.css')
    url_for('static', filename='assets/vendor/venobox/venobox.css')
    url_for('static', filename='assets/vendor/owl.carousel/assets/owl.carousel.min.css')
    url_for('static', filename='assets/vendor/aos/aos.css')
    url_for('static', filename='/assets/css/style.css')
    return render_template('index.html', article=article)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=os.getenv('PORT'))