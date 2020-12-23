from datetime import datetime

import requests
import configparser
import os

# from requests import ReadTimeout

bp = os.path.dirname(os.path.realpath('.')).split(os.sep)
url_config_file_path = os.sep.join(bp + ['reqres', 'config.ini'])
session = requests.session()
config = configparser.ConfigParser()
config.optionxform = str
config.read(url_config_file_path)


def get(url, input_data=None):
    try:
        print(datetime.now())
        response = session.get(url, params=input_data, timeout=config.getint('OTHERS', 'timeout'))
        print(datetime.now())
        # response.raise_for_status()
        return response.status_code, response.json(), response.reason
    except ConnectionError:
        print('Connection error')


def post(url, input_data):
    response = session.post(url, data=input_data, timeout=config.getint('OTHERS', 'timeout'))
    return response.status_code, response.json(), response.reason


def full_update(url, input_data):
    response = session.put(url, data=input_data, timeout=config.getint('OTHERS', 'timeout'))
    return response.status_code, response.json(), response.reason


def partial_update(url, input_data):
    response = session.patch(url, data=input_data, timeout=config.getint('OTHERS', 'timeout'))
    return response.status_code, response.json(), response.reason


def delete(url):
    response = session.delete(url)
    return response.status_code, response.reason
