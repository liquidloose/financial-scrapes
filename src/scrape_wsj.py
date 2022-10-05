'''
Calls upon playwright to open web page.
'''
from spreadsheet_editor import ExcelSheetCreator
from emailer import SendEmail
from data_parser import WSJParser
from playwright.async_api import async_playwright
import sys
import logging
import json
from dataclasses import asdict
import asyncio
from settings import PathData

print(PathData.asset_folder)


logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger(__name__)

logger.info('Scrape Initialized')


async def main():
    '''
    Opens web page and sends page html to parser
    '''
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.wsj.com/market-data/stocks/\
            marketsdiary?id=%7B%22application%22%3A%22WSJ \
            %22%2C%22marketsDiaryType%22%3A%22diaries%22%7D&type=mdc_marketsdiary')
        await page.wait_for_timeout(1000)
        html = await page.content()
        html_string = (str(html))

        data = WSJParser(html_string)
        data_dict = asdict(data)

        ExcelSheetCreator(data_dict, PathData.asset_folder)
        send_email = SendEmail()
        send_email.send()

        logger.info("The scrape has completed")

if __name__ == "__main__":
    asyncio.run(main())
