from app import app
import urllib.request,json
from models import Source
from models import Article



#Getting api key
api_key = app.config['SOURCE_API_KEY']

#Getting the source base url
base_url = app.config['SOURCE_API_BASE_URL']

#Getting the articles base url

articles_base_url = app.config['ARTICLES_API_BASE_URL']


def get_sources():
    '''
    Function that gets the json response to our url
    request.
    '''
    get_sources_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        source_results = None
        
        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
            
    return source_results

def process_results(source_list):
    '''
    Function that processes the source result and
    transforms them to a list of objects
    
    Args:
        source_list: A list of dictionaries that contain source details
        
    Returns:
        A list of source Objects
    '''
    source_results = []
    
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
        
        if id:
            source_object = Source(id,name,description,category)
            source_results.append(source_object)
        
    return source_results

def get_articles(id):
    get_source_articles_url = articles_base_url.format(id,api_key)
    
    with urllib.request.urlopen(get_source_articles_url) as url:
        
        source_articles_data = url.read()
        source_articles_response = json.loads(source_articles_data)
        
        article_object = None
    
        if source_articles_response['articles']:
            source_articles_list = source_articles_response['articles']
            article_object = process_articles(source_articles_list)
            
        
            
            
    return article_object

def process_articles(article_list):
    '''
    Function to take in the source object list and return the article object
    '''
    article_object = []



    for article_item in article_list:
            author = article_item.get('author')
            title = article_item.get('title')
            publishedAt = article_item.get('publishedAt')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            name = article_item.get('name')
            
            if description:   
                article_result = Article(author,title,publishedAt,description,url,urlToImage,name)
                article_object.append(article_result)
    
    return article_object
                
            