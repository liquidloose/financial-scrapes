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

    def wsj_data(self):
        '''
        Returns a dataframe containing NYSE data
        '''

        df1 = pd.DataFrame(self.data['nasdaq_data'])
        df1.drop('previousClose', axis=1, inplace=True)
        df1.drop('weekAgo', axis=1, inplace=True)

        print(df1)
        return df1

    @ staticmethod
    def data_connector(data_1):
        '''

        '''
        data_1.insert(3, " ", ["Scraped @", time.strftime("%b %d, %Y")])

        print(data_1.info(verbose=True))
        return data_1

    def writer(self):
        logger.info('Creating initial file')
        print('Creating initial file')
        # df = pd.concat([self.wsj_data()])
        formatted_data = self.wsj_data().T

        # contains just the essential data
        essential_data = formatted_data.iloc[1: 3]
        essential_data.to_excel('wsj.xlsx', index=True, header=False)
