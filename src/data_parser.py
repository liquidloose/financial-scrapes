'''
Parsing class that takes html input and extracts specific data.
'''
import json
import logging
import re
import time


logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


class WSJParser:
    '''
    Parses data from the NYSE
    '''

    def __init__(self, data):
        self.data = data

    def parsed_nyse_data(self):
        '''
        Latest close data.
        '''
        match = re.search('({.*)(\\\"}}\"})', self.data)
        json_data = json.loads(match.group())
        base_data = json_data["data"]["instrumentSets"]
        nyse_header = base_data[0]["headerFields"][0]["label"]
        nyse_data = base_data[0]["instruments"]
        nasdaq_header = base_data[1]["headerFields"][0]["label"]
        nasdaq_data = base_data[1]["instruments"]
        return [nyse_header, nyse_data, nasdaq_header, nasdaq_data]
