import os
from flask import Flask, render_template, url_for, send_from_directory, abort
app = Flask(__name__)

@app.route('/')
def index():
    f = open("/usr/src/app/templates/index.html", "r")
    file = f.read()
    return render_template('index.html', title = "Index", css="style.css", template=file)

@app.route('/<filename>')
def download_file(filename):
    return send_from_directory('/usr/src/app/pdf/',
                               filename, as_attachment=True)


@app.route('/article')
@app.route('/article<article>')
def hello(article):
    if int(article) > 0 and int(article) < 5:
        f = open("/usr/src/app/static/assets/articles/" + article + ".txt", "r")
        baseFile=open("/usr/src/app/templates/article.html", "r")
        file = baseFile.read()
        title = f.readline()
        article = f.readline()
        imagePath = f.readline()
        return render_template('article.html',
            css="style.css",
            template=file,
            title=title, 
            textArticle=article,
            imagePath=imagePath)
    else:
        return index()

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=os.getenv('PORT'))