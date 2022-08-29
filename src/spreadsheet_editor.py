import datetime
from pathlib import Path
import pandas as pd


test = {'nyse_header': 'NYSE', 'nyse_data': [{'id': 'issuestraded', 'name': 'Issues traded', 'latestClose': '3,364', 'previousClose': '3,397', 'weekAgo': '3,318'}, {'id': 'advances', 'name': 'Advances', 'latestClose': '429', 'previousClose': '2,548', 'weekAgo': '467'}, {'id': 'declines', 'name': 'Declines', 'latestClose': '2,750', 'previousClose': '663', 'weekAgo': '2,714'}, {'id': 'unchanged', 'name': 'Unchanged', 'latestClose': '185', 'previousClose': '186', 'weekAgo': '137'}, {'id': 'newhighs', 'name': 'New highs', 'latestClose': '28', 'previousClose': '43', 'weekAgo': '26'}, {'id': 'newlows', 'name': 'New lows', 'latestClose': '97', 'previousClose': '34', 'weekAgo': '57'}, {'id': 'advvolume', 'name': 'Adv. volume*', 'latestClose': '54,705,277', 'previousClose': '621,395,133', 'weekAgo': '129,345,359'}, {'id': 'declvolume', 'name': 'Decl. volume*', 'latestClose': '737,687,661', 'previousClose': '94,233,192', 'weekAgo': '735,146,805'}, {'id': 'totalvolume', 'name': 'Total volume*', 'latestClose': '795,074,490', 'previousClose': '723,716,291', 'weekAgo': '874,180,708'}, {'id': 'closingarmstrin', 'name': 'Closing Arms (TRIN)†', 'latestClose': '1.48', 'previousClose': '0.69', 'weekAgo': '0.89'}, {'id': 'blocktrades', 'name': 'Block trades*', 'latestClose': '3,962', 'previousClose': '3,926', 'weekAgo': '4,785'}, {'id': 'advvolume', 'name': 'Adv. volume', 'latestClose': '363,730,223', 'previousClose': '2,996,214,054', 'weekAgo': '601,748,210'}, {'id': 'declvolume', 'name': 'Decl. volume', 'latestClose': '3,461,342,328', 'previousClose': '534,929,523', 'weekAgo': '3,128,870,998'}, {
    'id': 'totalvolume', 'name': 'Total volume', 'latestClose': '3,849,184,279', 'previousClose': '3,573,440,396', 'weekAgo': '3,770,768,728'}], 'nasdaq_header': 'NASDAQ', 'nasdaq_data': [{'id': 'issuestraded', 'name': 'Issues traded', 'latestClose': '4,851', 'previousClose': '4,903', 'weekAgo': '4,762'}, {'id': 'advances', 'name': 'Advances', 'latestClose': '807', 'previousClose': '3,111', 'weekAgo': '987'}, {'id': 'declines', 'name': 'Declines', 'latestClose': '3,744', 'previousClose': '1,499', 'weekAgo': '3,542'}, {'id': 'unchanged', 'name': 'Unchanged', 'latestClose': '300', 'previousClose': '293', 'weekAgo': '233'}, {'id': 'newhighs', 'name': 'New highs', 'latestClose': '37', 'previousClose': '53', 'weekAgo': '46'}, {'id': 'newlows', 'name': 'New lows', 'latestClose': '172', 'previousClose': '99', 'weekAgo': '109'}, {'id': 'closingarmstrin', 'name': 'Closing Arms (TRIN)†', 'latestClose': '1.01', 'previousClose': '0.74', 'weekAgo': '1.24'}, {'id': 'blocktrades', 'name': 'Block trades', 'latestClose': '25,123', 'previousClose': '27,938', 'weekAgo': '28,781'}, {'id': 'advvolume', 'name': 'Adv. volume', 'latestClose': '796,751,531', 'previousClose': '3,127,993,378', 'weekAgo': '838,451,308'}, {'id': 'declvolume', 'name': 'Decl. volume', 'latestClose': '3,730,433,337', 'previousClose': '1,108,149,981', 'weekAgo': '3,728,895,732'}, {'id': 'totalvolume', 'name': 'Total volume', 'latestClose': '4,543,505,642', 'previousClose': '4,264,125,531', 'weekAgo': '4,598,836,075'}]}

# del test['nyse_data']
# del test['nasdaq_data'][8:]


class ExcelWriter:
    def __init__(self, data):
        self.data = data
        self.file_check()

    def file_check(self):
        path_exists = Path("/var/www/financial-scrapes/wsj.xlsx")
        if path_exists.is_file():
            print('File exists!')
        else:
            print('No file exists')
            self.writer(write_headers=True)

    def nyse_dataframe(self):

        df1 = pd.DataFrame(self.data['nasdaq_data'])
        df1['grade'] = 'A'
        df1.drop('previousClose', axis=1, inplace=True)
        df1.drop('weekAgo', axis=1, inplace=True)
        df1 = df1.iloc[:, 1:]
        df1_transposed = df1.T
        # df1_transposed.to_excel('wsj.xlsx', index=False)
        # return df1_transposed.to_excel('wsj.xlsx', index=False)
        return df1_transposed

    def nasdaq_dataframe(self):

        df1 = pd.DataFrame(self.data['nasdaq_data'])
        df1.drop('previousClose', axis=1, inplace=True)
        df1.drop('weekAgo', axis=1, inplace=True)
        df1 = df1.iloc[:, 1:]
        df1_transposed = df1.T
        return df1_transposed

    def exchange_info(self):

        timestamp = datetime.datetime.now()
        header_one = [self.data['nyse_header'], timestamp]
        header_two = [self.data['nasdaq_header'], timestamp]
        df1 = pd.DataFrame(header_one)
        return df1

    @staticmethod
    def multiple_dfs(df_list):
        for dataframe in df_list:
            dataframe.to_excel('wsj.xlsx')

    def writer(self, write_headers=False):
        if write_headers == True:
            print('Writing to file with headers')
            df = pd.concat(
                [self.exchange_info(), self.nyse_dataframe(), self.nasdaq_dataframe()], axis=1)
            df.to_excel('wsj.xlsx', index=False)


test = ExcelWriter(test)
# test.nyse()
