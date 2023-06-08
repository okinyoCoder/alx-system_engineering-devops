#!/usr/bin/python3

"""function that queries the Reddit API and returns
   the number of subscribers for a given subreddit.
   If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/320.41'}
    res = requests.get(url, headers=headers)
    print(res.json)
    if res.status_code != 200:
        return (0)
    res = res.json()
    if 'data' in res:
        return (response.get('data').get('subscribers'))

    else:
        return (0)
