#!/usr/bin/env python3

import sys
import requests


YEAR = '2020'


def get_input_string(day):
    session = requests.Session()
    with open('.token') as fd:
        token = fd.read().strip()
    url = f'http://adventofcode.com/{YEAR}/day/{day}/input'
    resp = session.get(url, cookies={'session': token})
    return resp.text


def download_input_file(day):
    with open(f'/home/fay/code/adventofcode/{YEAR}/input.txt', 'w') as f:
        f.write(get_input_string(day))


def read_file(file):
    with open(file) as f:
        return f.read()


if __name__ == '__main__':
    download_input_file(sys.argv[1])
