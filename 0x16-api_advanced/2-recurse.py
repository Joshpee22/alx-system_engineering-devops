#!/usr/bin/python3
"""
Using Reddit's API
"""
import requests

after = None

def recurse(subreddit, hot_list=[]):
    """Return top ten post titles recursively"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent, allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
        else:
            return hot_list  # No more data, return the list
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return recurse(subreddit, hot_list)  # Make the recursive call unconditionally
    else:
        return None
