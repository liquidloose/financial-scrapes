'''
Runs tests
'''
import logging
from src.scraper.file_scanner import FileScanner


logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger(__name__)


# @pytest.mark.asyncio
# async def test_main_scraper():
#'''initiates scraper test'''
#    assert await main() == 0

logger.info('before scanner test')


def test_file_scanner():
    '''
    Checks the FileScanner class
    '''
    scanner = FileScanner()
    #html = scanner.get_html()
    logger.info(scanner.get_html())
    assert len(scanner.get_html()) > 0

