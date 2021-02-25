from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index
    page and its data
    '''
    
    return render_template('index.html')

@app.route('/news/<news_url>')
def news(news_url):
    '''
    View news page function that returns news details
    '''
    return render_template('news.html',url=news_url)