'''
Calls upon playwright to open web page.
'''
import asyncio
import json
import logging
from bs4 import BeautifulSoup as Soup
from playwright.async_api import async_playwright

from data_parser import WSJParser


logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger(__name__)

logger.info('Scrape Initialized')


async def main():
    '''
    Opens web page and sends page html to parser
    '''

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.wsj.com/market-data/stocks/marketsdiary?id=%7B%22application%22%3A%22WSJ \
            %22%2C%22marketsDiaryType%22%3A%22diaries%22%7D&type=mdc_marketsdiary')

        html = await page.content()
        html_string = (str(html))
        soup = Soup(html, "html.parser")
        # print(soup)

        await page.wait_for_timeout(1000)

        nyse = WSJParser(html_string)
        # print(html_string)
        print(nyse.parsed_nyse_data())

        logger.info("The scrape has completed")

if __name__ == "__main__":
    asyncio.run(main())
