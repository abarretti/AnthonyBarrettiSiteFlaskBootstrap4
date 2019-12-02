import os
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

## PROD URL
# url = 'https://anthonybarretti.com'
## TEST URL
url = 'http://0.0.0.0:8080'
now = datetime.utcnow()

@app.route("/")
@app.route("/home")
def home():
    dir = ''
    return render_template('home.html', url = url, now = now, dir = dir)

@app.route("/about")
def about():
    dir = 'about'
    return render_template('about.html', url = url, now = now, dir = dir)

@app.route("/cv")
def cv():
    dir = 'cv'
    return render_template('cv.html', url = url, now = now, dir = dir)

@app.route("/contact")
def contact():
    dir = 'contact'
    return render_template('contact.html', url = url, now = now, dir = dir)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
