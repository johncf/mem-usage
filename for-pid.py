#!/usr/bin/env python3

import psutil
import time
from sys import argv


def main(pid: int):
    """prints epoch-time and RSS (in bytes) once every second"""
    p = psutil.Process(pid)
    while True:
        rss = get_rss(p)
        if not rss:
            break
        for c in p.children(True):
            rss += get_rss(c)
        print(f"{int(time.time())} {rss}")
        time.sleep(1)


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
