from flask import Flask, render_template, request, redirect, url_for
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/sections')
def sections():
    return render_template('pages/sections.html')

@app.route('/news')
def news():
    return render_template('pages/news.html')

@app.route('/results')
def results():
    return render_template('pages/results.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

if __name__ == '__main__':
    app.run(debug=True)
