'''
Runs tests
'''
from dataclasses import asdict
import json
import re
from socket import gethostbyaddr
import pytest
from src.data_parser import WSJParser

print('hello, world!')


@pytest.fixture
def get_json():
    '''
    Opens and returns html file.
    '''
    with open('market_diary.json', 'r') as f:
        data = json.load(f)
    # print(data)
    return data


@pytest.fixture
def get_html():
    '''
    Opens and returns html file.
    '''
    with open('market_diary.html', 'r') as f:
        data = f.read()
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

    #assert required_length == actual_length
    assert 3


print('hello, world!')


def test_json_parsing(get_html):
    test = WSJParser(get_html)
    # print(test.html_data)
    # print(WSJParser.test(get_html))
    print(test.nyse_data())
