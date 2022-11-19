import threading
import os, re
import sys
import time

def thread_job():
    global counter
    global res
    old_counter = counter
    counter = old_counter + 1
    res += array[old_counter]

array = []
for i in range(100):
    array.append(i)

def programm_run(num):
    print(f"Num: {num}")
    lock = threading.Lock()
    global counter
    global res
    counter = 0
    res = 0
    start_time = time.time()
    threads = [threading.Thread(target=thread_job) for _ in range(num)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    print(f"Time: {time.time() - start_time}")
    print(res)

for i in range(1, 10):
    programm_run(i*10)