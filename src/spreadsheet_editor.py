from tabnanny import verbose
import numpy as np
import pandas as pd
import time
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger(__name__)


class ExcelWriter:
    def __init__(self, data):
        self.data = data
        self.file_check()

    def __str__(self):
        return "ExcelWriter Object"

    def file_check(self):
        '''
        Checks if the excel file exists. If it doesn't exist, a header row 
        is added to the spreadsheet.
        '''
        path_exists = Path("/var/www/financial-scrapes/wsj.xlsx")
        if path_exists.is_file():
            print('File exists!')
            logger.info('File exists!')
        else:
            logger.info('No file exists yet')
            print('No file exists')
            self.writer()

    def nyse_dataframe(self):
        '''
        Returns a dataframe containing NYSE data
        '''

        df1 = pd.DataFrame(self.data['nasdaq_data'])
        df1.drop('previousClose', axis=1, inplace=True)
        df1.drop('weekAgo', axis=1, inplace=True)

        print(df1)
        df1 = df1.iloc[:, 1:]
        df1_transposed = df1.T
        # 0, " ", ["Scraped @", time.strftime("%b %d, %Y")])
        print(df1_transposed)
        # df1_transposed.to_excel('wsj.xlsx', index=False)
        # return df1_transposed.to_excel('wsj.xlsx', index=False)
        print(df1_transposed.info(verbose=True))

        return df1_transposed

    @staticmethod
    def data_connector(data_1):
        '''

        '''
        data_1.insert(3, " ", ["Scraped @", time.strftime("%b %d, %Y")])

        #data_1.loc[-1] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]
        print(data_1.info(verbose=True))
        return data_1

    def writer(self):
        logger.info('Creating initial file')
        print('Creating initial file')
        #df = pd.concat([self.nyse_dataframe()])
        formatted_data = self.data_connector(
            self.nyse_dataframe())

        print(formatted_data)
        formatted_data.to_excel('wsj.xlsx', index=False)
