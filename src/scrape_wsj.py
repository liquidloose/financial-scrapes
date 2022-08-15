
'''
Calls upon playwright to open web page.
'''
from hashlib import new
import asyncio
import logging
from bs4 import BeautifulSoup as Soup
from playwright.async_api import async_playwright
from data_parser import HTMLParser

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
        await page.goto('https://www.wsj.com/market-data/stocks/marketsdiary?\
                fbclid=IwAR0gD9HYW8CFy70OJCsWVXIfjMep_XtoZ4RjzGCTpCDSmq4LXeYcQkHYizY')

        await page.wait_for_timeout(1000)
        html = await page.content()
        if html:
            logger.info('Page has successfully been loaded.')
        soup = Soup(html, 'html.parser')
        parse = HTMLParser(soup)
        logger.info(parse.title())
        logger.info(soup.title)

        await browser.close()
        name = 'ron'
        assert name == 'ron'
        logger.info("The scrape has completed")
    return 'ron'

if __name__ == "__main__":
    asyncio.run(main())
