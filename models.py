class Source:
    '''
    Source class to define the source objects
    '''
    
    def __init__(self,id,name,description,category):
        self.id = id
        self.name = name 
        self.description = description
        self.category = category
        
class Article:
    '''
    Article class to define the article objects
    '''
    
    def __init__(self,author,title,publishedAt,description,url,urlToImage,name):
        self.author = author
        self.title = title
        self.publishedAt = publishedAt
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.name = name