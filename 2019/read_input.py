#!/usr/bin/env python3

import requests
import sys


def get_input_string(day):
    session = requests.Session()
    with open('.token') as fd:
        token = fd.read().strip()
    url = 'http://adventofcode.com/2019/day/{}/input'.format(day)
    resp = session.get(url, cookies={'session': token})
    return resp.text


def download_input_file(day):
    with open('/home/fay/code/adventofcode/2019/input.txt', 'w') as f:
        f.write(get_input_string(day))


def get_input_string_from_file(file):
    with open(file) as f:
        return f.read()


if __name__ == '__main__':
    download_input_file(sys.argv[1])