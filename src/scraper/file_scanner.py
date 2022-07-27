'''
Returns an html file's contents as a string
'''
import logging
import os

from tomlkit import string

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger(__name__)


class FileScanner:
    '''
    Returns a list of file names from the html folder.
    '''

    def __init__(self) -> list[string]:
        pass

    def get_html(self):
        '''
        Returns list of file names in the html directory
        '''

        path = '../src/scraper/html'
        obj = os.scandir(path)
        file_name_list = []

        for entry in obj:
            if entry.is_dir() or entry.is_file():
                # print(entry.name)
                file_name_list.append(entry.name)
        logger.info('Files scanned')
        return file_name_list


testing = FileScanner()
print(testing.get_html())