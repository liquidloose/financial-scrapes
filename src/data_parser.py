'''
Parsing class that takes html input and extracts specific data.
'''
from dataclasses import InitVar, dataclass, field
from email.policy import default
import json
import logging
import re
from reprlib import Repr
import time
from typing import ClassVar


logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


@dataclass
class WSJParser:
    '''
    Parses data from the NYSE
    '''
    html_data: InitVar[str] = None
    base_data: InitVar[str] = None
    nyse_header: str = field(init=False)
    nyse_data: str = field(init=False)
    nasdaq_header: str = field(init=False)
    nasdaq_data: str = field(init=False)

    def __post_init__(self, html_data, base_data):
        base_data = self.base_data_parser(html_data)
        self.nyse_header = self.nyse_header_parser(base_data)
        self.nyse_data = self.nyse_data_parser(base_data)
        self.nasdaq_header = self.nasdaq_header_parser(base_data)
        self.nasdaq_data = self.nasdaq_data_parser(base_data)

    @staticmethod
    def base_data_parser(data):
        regex = '({.*)(\\\"}}\"})'
        match = re.search(regex, data)
        json_data = json.loads(match.group())
        base_data = json_data["data"]["instrumentSets"]
        return base_data

    @staticmethod
    def nyse_header_parser(data):
        nyse_header = data[0]["headerFields"][0]["label"]
        return nyse_header

    @staticmethod
    def nyse_data_parser(data):
        nyse_data = data[0]["instruments"]
        return nyse_data

    @staticmethod
    def nasdaq_header_parser(data):
        nasdaq_header = data[1]["headerFields"][0]["label"]
        return nasdaq_header

    @staticmethod
    def nasdaq_data_parser(data):
        nasdaq_data = data[1]["instruments"]
        return nasdaq_data
