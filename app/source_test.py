import unittest
from models import source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test
        '''
        self.new_source = Source('abc-news','ABC NEWS',"Australia's most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
        
        
if __name__ == '__main__':
    unittest.main()      