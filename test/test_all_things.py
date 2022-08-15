'''
Runs tests
'''
import logging
import sys
import pytest


print(sys.path)
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger(__name__)
logger.warning('hiasdfasdfasdf')

# @pytest.mark.asyncio
# async def test_main_scraper():
#'''initiates scraper test'''
#    assert await main() == 0


@pytest.fixture
def get_html():
    '''
    Opens and returns html file.
    '''
    print('coming straigt atchya from the get_html fixture!!!')
    with open('markets_diary.html', 'r', encoding='utf-8') as f:
        print(f.read())
    return f


def test_html_exists(get_html):
    '''
    Checks to see if the html file exists.
    '''
    assert get_html
