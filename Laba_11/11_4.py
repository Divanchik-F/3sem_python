import threading
import os, re
import sys
import time
import urllib.request

def thread_job():
    global counter
    old_counter = counter
    counter = old_counter + 1
    with urllib.request.urlopen(urls(old_counter)) as u:
        return u.read()

counter = 0

urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()
for url in urls:
    read_url(url)
print(f"Without threading: {time.time() - start}")


start = time.time()

threads = [threading.Thread(target=thread_job) for _ in range(len(urls))]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f"With threading: {time.time() - start}")