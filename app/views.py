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
    business_news = get_sources('business')
    print(business_news)
    
    title = 'Home - Welcome to the Website that keeps you updated on whats happening in the world.'
    return render_template('index.html',title = title,business = business_news)

@app.route('/article/<id>')
def article(id):
     '''
     View news page function that returns source articles
     '''
     article = get_articles(id)
     
   
    
     return render_template('article.html',article = article)