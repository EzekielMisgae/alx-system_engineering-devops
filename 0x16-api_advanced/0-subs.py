#!/usr/bin/python3
"""function to get the number of subscribers in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """gets the number of subscribers"""
    if subreddit is None:
        return 0
    data = requests.get('http://www.reddit.com/r/{}/about.json'
                        .format(subreddit),
                        headers={"User-Agent": 'alx'}).json()
    try:
        nos = data.get('data').get('subscribers', 0)
        return nos
    except Exception:
        return 0
