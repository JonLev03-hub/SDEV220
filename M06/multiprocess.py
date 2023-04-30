import multiprocessing
import time
import random
from datetime import datetime as dt


def myFunc():
    sleep_time = random.random()
    time.sleep(sleep_time)
    current_time = dt.now().strftime("%H:%M:%S")
    print(f"{multiprocessing.current_process().name} Slept for: {sleep_time:.2f}s Finished At: {current_time}")


if __name__ == '__main__':
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=myFunc, name=f"Process {i+1}")
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
