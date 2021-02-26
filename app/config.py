class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    ARTICLES_API_BASE_URL ='http://newsapi.org/v2/everything?sources={}&sortBy=publishedAt&apiKey={}'


class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general
        configuration settings
        
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general
        configuration settings
        
    '''
    
    DEBUG = True
        