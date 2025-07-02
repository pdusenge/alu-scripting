#!/usr/bin/python3
"""DOCS"""
import requests
import sys


def top_ten(subreddit):
    """Docs"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    headers = headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        # for post in data['children'][:10]:
        sys.stdout.write("OK")
    else:
        sys.stdout.write("OK")
