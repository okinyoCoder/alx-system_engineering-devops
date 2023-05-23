#!/usr/bin/python3
"""Gets data from API"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        url = 'https://jsonplaceholder.typicode.com'
        nu = argv[1]
        '''getting username from api'''
        r = requests.get('{}/users/{}'.format(url, nu))
        name = r.json().get('name')
        '''getting total number of task'''
        req = requests.get('{}/todos?userId={}'.format(url, nu))
        task = req.json()
        total_task = len(task)
        count = 0
        lizt = []
        for obj in task:
            if obj.get('completed') is True:
                count = count + 1
                lizt.append(obj.get('title'))
        print('Employee {} is done with tasks ({}/{})'.format(
            name, count, total_task))

        for i in lizt:
            print('\t {}'.format(i))
