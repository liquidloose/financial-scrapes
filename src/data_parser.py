'''
Parsing class that takes html input and extracts specific data.
'''
from dataclasses import dataclass
import json
import logging
import re
import time
from typing_extensions import Self


logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


@dataclass
class WSJParser:
    '''
    Parses data from the NYSE
    '''
    html_data: str
    regex: str = '({.*)(\\\"}}\"})'

    def base_data(self):
        match = re.search(self.regex, self.html_data)
        json_data = json.loads(match.group())
        base_data = json_data["data"]["instrumentSets"]
        return base_data

    def nyse_header(self):
        nyse_header = self.base_data()[0]["headerFields"][0]["label"]
        return nyse_header

    def nyse_data(self):
        nyse_data = self.base_data()[0]["instruments"]
        return nyse_data

    def nasdaq_header(self):
        nasdaq_header = self.base_data()[1]["headerFields"][0]["label"]
        return nasdaq_header

    def nasdaq_data(self):
        nasdaq_data = self.base_data()[1]["instruments"]
        return nasdaq_data
