class Config:
    '''
    General configuration parent class
    '''
    pass


class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general
        configuration settings
        
    '''
    SOURCE_BASE_API_URL = 'https://newsapi.org/v2/sources?apiKey={}'

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general
        configuration settings
        
    '''
    
    DEBUG = True
        