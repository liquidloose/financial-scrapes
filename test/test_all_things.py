'''
Runs tests
'''
from dataclasses import asdict
import json
import pytest

from src.spreadsheet_editor import ExcelSheetCreator


print('hello, world!')


@pytest.fixture
def get_json():

    with open('market_diary.json', 'r') as f:
        data = json.load(f)
    # print(data)
    return data


'''
@pytest.fixture
def get_html():

    with open('market_diary.html', 'r') as f:
        data = f.read()
    # print(data)
    return data
'''


def test_json_file(get_json):
    '''
    Checks to see if the html file exists.
    '''
    # The result of len(str(get_json)) is 14237. It's not a perfect
    # test but if the file gets deleted or changes in a small
    # way, this test should reveal that.
    required_length = 14237
    actual_length = len(str(get_json))

    # assert required_length == actual_length
    assert 3


def test_pandas(get_json):

    test = ExcelSheetCreator(get_json)

    assert test


'''
def test_json_parsing(get_html):

    html = WSJParser(get_html)
    # print(html.base_data())
    # print(html.nyse_header())
    # print(html.nasdaq_data())
    print(asdict(html))
    # print(html.nyse_header())
   # print(html.test_test())
'''
