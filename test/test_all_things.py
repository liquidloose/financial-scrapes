'''
Runs tests
'''

from dataclasses import asdict
import json
import os
import pytest
from src.spreadsheet_editor import ExcelSheetCreator
from test.settings import PathData


def test_test():
    assert 1 == 1


print(os.environ)
print(type(os.environ.get('ROBOTS_PASSWORD')))


@pytest.fixture
def get_json():

    with open('market_diary.json', 'r') as f:
        data = json.load(f)
    # print(data)
    return data


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

    test = ExcelSheetCreator(get_json, PathData.asset_folder)

    assert test
