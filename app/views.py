from flask import render_template
from app import app
from .request import get_sources

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

#@app.route('/news/<news_url>')
#def news(news_url):
 #   '''
  #  View news page function that returns news details
   # '''
    #title = 'News- View related articles'
    
   # return render_template('news.html',url=news_url,title = title)