import functools
from pympler import asizeof
import requests


def memory_using(f):
    @functools.wraps(f)
    def deco(*args, **kwargs):
        result = f(*args, **kwargs)
        print(f'({f.__name__}): {asizeof.asizeof(result)} Bytes memory using')
        return result
    return deco


@memory_using
def fetch_url(url, first_n=100555):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

fetch_url('https://google.com')