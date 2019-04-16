#!/usr/bin/env python3

import psutil
import random
import time
from sys import argv, stdout


def main(pid: int):
    """prints epoch-time, number of processes, and RSS (in bytes) once every second"""
    p = psutil.Process(pid)
    while True:
        rss = get_rss(p)
        if not rss:
            break
        num_proc = 1
        for c in p.children(True):
            rss += get_rss(c)
            num_proc += 1
        print(f"{int(time.time())} {num_proc} {rss}")
        time.sleep(1)
        if random.randint(1, 20) == 1:
            stdout.flush()


def get_rss(proc):
    try:
        return proc.memory_info().rss
    except psutil.NoSuchProcess:
        return 0


if __name__ == '__main__':
    if len(argv) != 2:
        print(f"Usage {argv[0]} PID")
    else:
        main(int(argv[1]))
