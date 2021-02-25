from flask import render_template
from app import app
from .request import get_sources,get_articles

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index
    page and its data
    '''
    #Getting sources
    news_sources = get_sources()
    print(news_sources)
    
    title = 'Home - Welcome to the Website that keeps you updated on whats happening in the world.'
    return render_template('index.html',title = title,news = news_sources)

@app.route('/article/<id>')
def article(id):
     '''
     View news page function that returns source articles
     '''
     article = get_articles(id)
     title = f'{article.title}'
    
    return render_template('article.html',title = title,article = article)