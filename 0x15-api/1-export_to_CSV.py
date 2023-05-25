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
        print(name)
        '''getting total number of task'''
        req = requests.get('{}/todos?userId={}'.format(url, nu))
        tasks = req.json()

        with open('{}.csv'.format(employeeId), 'w') as file:
            for task in tasks:
                file.write('"{}","{}","{}","{}"\n'.format(
                    nu,
                    name,
                    task.get('completed'),
                    task.get('title')))
