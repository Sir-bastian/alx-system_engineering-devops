#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the
number of subscribers (not active) user, total subscribers)
for a given subreddit. If an invalid subreddit isgiven, the
function should return 0
"""
import requests
import sys


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if str(response) != '<Response [200]>':
        return 0

    r_json = response.json()
    num_subs = r_json.get("data").get("subscribers")
    return num_subs
