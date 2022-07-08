'''
Connects to designated website and prints the page html.
'''
from playwright.async_api import async_playwright


def stream():
    '''Tries to yield a stream'''
    print('this is the stream lolz')
    yield 'crap'


async def output(page):
    print(page.url)
    print('that was the url of the page broski')
    return stream()


async def scrape():
    '''
    Launches browser and calls the crawler.
    '''
    async with async_playwright() as play_wright:
        browser = await play_wright.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.wsj.com/market-data/stocks/marketsdiary?\
            fbclid=IwAR0gD9HYW8CFy70OJCsWVXIfjMep_XtoZ4RjzGCTpCDSmq4LXeYcQkHYizY')
        print(page)
        await output(page)
        await browser.close()
