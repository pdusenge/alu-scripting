#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Main function"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {'User-Agent': 'Python:top_ten:v1.0 (by /u/yourusername)'}
        params = {'limit': 10}

        try:
            response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False,
                timeout=10
            )

            if response.status_code != 200:
                print(None)
                return

            data = response.json().get('data', {}).get('children', [])

            if not data:
                print(None)
                return

            for post in data:
                print(post.get('data', {}).get('title'))

        except Exception:
            print(None)
