import collections
import aiohttp
import asyncio
from pprint import pprint

urls = [
    "add",
    "urls",
    "here"
]


def compare_all(iterable, key=None):
    if not isinstance(iterable, collections.Iterator):
        iterable = iter(iterable)
    first = next(iterable)
    return all([key(it, first) for it in iterable])


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def fetch_json_from_url(url):
    async with aiohttp.ClientSession() as session:
        print("AWAITING", url)
        json_resp = await fetch(session, url)
        return dict(json_resp)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(
        *[fetch_json_from_url(url) for url in urls]))
    res = compare_all(results, key=lambda i, p: i == p)
    if res:
        print("\n")
        pprint(results[0])
        print("\n")
    print("Comparison result= *{}*".format(str(res).upper()))
