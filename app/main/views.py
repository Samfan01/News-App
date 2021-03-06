from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles

#Views
@main.route('/')
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

@main.route('/article/<id>')
def article(id):
     '''
     View news page function that returns source articles
     '''
     article = get_articles(id)
     
   
    
     return render_template('article.html',article = article)