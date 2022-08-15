'''
Parsing class that takes html input and extracts specific data.
'''
import logging


logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


class HTMLParser:
    '''
    Parses site information
    '''

    def __init__(self, soup):
        self.soup = soup

    def title(self):
        '''
        soup printing test
        '''
        logger.info('Returned the title')
        return self.soup.title.contents
