from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index
    page and its data
    '''
    title = 'Home - Welcome to the Website that keeps you updated on whats happening in the world.'
    return render_template('index.html',title = title)

@app.route('/news/<news_url>')
def news(news_url):
    '''
    View news page function that returns news details
    '''
    title = 'News- View related articles'
    
    return render_template('news.html',url=news_url,title = title)