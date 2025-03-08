import requests
import functools

from collections import OrderedDict


def lfu_cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._cache.move_to_end(cache_key, last=True)
                deco._cache[cache_key] = (deco._cache[cache_key][0], deco._cache[cache_key][1] + 1)
                return deco._cache[cache_key][0]
            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                min_freq_key = min(deco._cache, key=lambda k: deco._cache[k][1])
                deco._cache.pop(min_freq_key)
            deco._cache[cache_key] = (result, 1)
            return result
        deco._cache = OrderedDict()
        return deco
    return internal


@lfu_cache
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

fetch_url('https://google.com')