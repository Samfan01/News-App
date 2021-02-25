import unittest
from models import article

Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Article('','','',0,'','')
        
        def test_instance(self):
            self.assertTrue(isinstance(self.new_article,Article))
            
            
if __name__ == '__main__':
    unittest.main()
