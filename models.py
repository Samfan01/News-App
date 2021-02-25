class Source:
    '''
    Source class to define the source objects
    '''
    
    def __init__(self,id,name,description):
        self.id = id
        self.name = name 
        self.description = description
class Article:
    '''
    Article class to define the article objects
    '''
    
    def __init__(self,author,title,publishedAt,description,url,urlToImage):
        self.author = author
        self.title = title
        self.publishedAt = publishedAt
        self.description = description
        self.url = url
        self.urlToImage = urlToImage