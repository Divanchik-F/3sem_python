from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service):
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as resp:
            res=await resp.json()
            return res[service.ip_attr]


async def asynchronous():
    ip_addr, smth=await asyncio.wait([fetch_ip(site) for site in SERVICES], return_when=FIRST_COMPLETED)
    for elem in ip_addr:
        print(elem.result())

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())