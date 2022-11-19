import threading
import sys


def thread_job():
    global counter
    old_counter = counter #Записываем текущеее значение counter в old_counter
    counter = old_counter + 1 #Пытаемся записать counter как old_counter + 1, но не учитываем,
                              #что другие потоки уже могли увеличить значение counter. Поэтому может быть
                              #такое, что текущее значение counter больше old_counter, и нашим действием
                              #мы можем не только не изменить значение counter, но и уменьшить его.
    print('{} '.format(counter), end='')
    sys.stdout.flush()


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)