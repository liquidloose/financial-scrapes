from importlib.metadata import metadata
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
        path_exists = Path("/var/www/financial-scrapes/test/wsj.xlsx")
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
    def data_injector(data_1, data_2):
        '''
        Inserts exchange names and scrape times into the data
        '''
        data_1.insert(
            0, " ", ["", "Exchange", "NYSE"])

        data_1.insert(
            0, " 2", ["", "Scraped On", time.strftime("%b %d, %Y")])

        data_1.insert(
            15, " ", ["", "Exchange", "NASDAQ"], allow_duplicates=True)

        data = pd.concat([data_1, data_2], axis=1)

        return data.iloc[1:3]

    def writer(self):
        '''
        Writes the data to an excel file
        '''

        file_exists = self.file_check()
        print(f"does the file exist? {file_exists}")

        data = self.wsj_data(self.data)

        sheet_data = self.data_injector(data[0], data[1])

        if file_exists is False:
            print('Creating file and writing data to it')
            logger.info('Creating file and writing data to it')
            sheet_data.to_excel(
                'wsj.xlsx', sheet_name="stock_data", index=False, header=False)
        elif file_exists is True:
            print('Appending data to file')
            logger.info('Appending data to file')
            with pd.ExcelWriter('wsj.xlsx', mode='a', if_sheet_exists='overlay') as writer:
                sheet_data.to_excel(writer, sheet_name="stock_data")
