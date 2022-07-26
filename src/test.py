
import logging
import pytest


from scrape import main


logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_main_scraper():
    '''initiates scraper test'''
    assert await main() == 0
