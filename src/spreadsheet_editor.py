from tabnanny import verbose
import numpy as np
import pandas as pd
import time
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger(__name__)


class ExcelSheetCreator:
    '''
    Takes in JSON, converts it into data frames and writes that
    data to an excel spreadsheet.
    '''

    def __init__(self, data):
        self.data = data
        # self.file_check()
        self.writer()

    def __str__(self):
        return "ExcelSheetCreator Object"

    @staticmethod
    def file_check():
        '''
        Checks if the excel file exists. If it doesn't exist, a header row
        is added to the spreadsheet.
        '''
        path_exists = Path("/var/www/financial-scrapes/wsj.xlsx")
        if path_exists.is_file():
            print('File exists!')
            logger.info('File exists!')
            return True
        else:
            logger.info('No file exists yet')
            print('No file exists')
            return False
            # self.writer()

    @staticmethod
    def wsj_data(data):
        '''
        Returns a two item list containing data related to NYSE and NASDAQ
        '''

        def drop(data_frame):
            data_frame.drop('previousClose', axis=1, inplace=True)
            data_frame.drop('weekAgo', axis=1, inplace=True)

        nyse_data = pd.DataFrame(data['nyse_data'])
        nasdaq_data = pd.DataFrame(data['nasdaq_data'])

        data = [nasdaq_data, nyse_data]
        for x in data:
            drop(x)

        # print(nyse_data)
        return [nyse_data.T, nasdaq_data.T]

    @staticmethod
    def data_injector(data_1, exchange_name):
        '''
        Inserts exchange names and scrape times into the data

        '''
        data_1.insert(
            0, " ", ["", "Exchange", exchange_name])

        if exchange_name == 'NYSE':
            data_1.insert(
                0, " 2", ["", "Scraped @", time.strftime("%b %d, %Y")])

        return data_1

    def writer(self):
        '''
        Writes the data to an excel file
        '''

        file_exists = self.file_check()

        # df = pd.concat([self.wsj_data()])
        data = self.wsj_data(self.data)
        nyse_data = data[0]
        nasdaq_data = data[1]
        print(nyse_data)
        print(nasdaq_data)

        # print(formatted_data)
        #test_data = self.data_injector(formatted_data, 'NYS2E')
        # print(test_data)
        # contains just the essential data
        #essential_data = formatted_data.iloc[1: 3]
        #essential_data.to_excel('wsj.xlsx', index=True, header=False)
