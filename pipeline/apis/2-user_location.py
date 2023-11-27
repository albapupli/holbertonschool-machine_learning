#!/usr/bin/env python3

"""
By using the GitHub API, write a script that prints the location of a specific user:

The user is passed as first argument of the script with the full API URL, example: ./2-user_location.py https://api.github.com/users/holbertonschool
If the user doesn’t exist, print Not found
If the status code is 403, print Reset in X min where X is the number of minutes from now and the value of X-Ratelimit-Reset
Your code should not be executed when the file is imported (you should use if __name__ == '__main__':)
"""

"""
Rate me is you can!
"""

import time
import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit()
    url = sys.argv[1]
    headers = {'Accept': 'application/vnd.github.v3+json'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        print(res.json()['location'])
    elif res.status_code == 403:
        rate_limit = int(res.headers['X-Ratelimit-Reset'])
        now = int(time.time())
        minutes = int((rate_limit - now) / 60)
        print("Reset in {} min".format(minutes))
    elif res.status_code == 404:
        print('Not found')
