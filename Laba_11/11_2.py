import threading
import sys
import os, re

received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

def thread_job():
    with lock:
        global suffix
        old_suffix = suffix
        suffix += 1
    ip = "192.168.178." + str(old_suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])

lock = threading.Lock()
suffix = 20
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()