from app import app
import urllib.request,json
from models import Source

#Source = source.Source

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
        
        if id:
            source_object = Source(id,name,description)
            source_results.append(source_object)
        
    return source_results

def get_articles(id):
    get_source_articles_url = articles_base_url.format(id,api_key)
    
    with urllib.request.urlopen(get_source_articles_url) as url:
        
        source_articles_data = url.read()
        source_articles_response = json.loads(source_articles_data)
        
        source_object = None
        if source_articles_response:
            
        