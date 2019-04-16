#!/usr/bin/env python3

import psutil
import random
import time
from sys import argv, stdout


def main(pid: int):
    """prints epoch-time, number of processes, RSS (bytes), and VMS (bytes) once every second"""
    p = psutil.Process(pid)
    while True:
        rss = get_rss(p)
        vms = get_vms(p)
        if not rss:
            break
        num_proc = 1
        for c in p.children(True):
            rss += get_rss(c)
            vms += get_vms(c)
            num_proc += 1
        print(f"{int(time.time())} {num_proc} {rss} {vms}")
        time.sleep(1)
        if random.randint(1, 20) == 1:
            stdout.flush()


def get_rss(proc):
    return get_prop(proc, 'rss')


def get_vms(proc):
    return get_prop(proc, 'vms')


def get_prop(proc, prop):
    try:
        return getattr(proc.memory_info(), prop, 0)
    except psutil.NoSuchProcess:
        return 0


if __name__ == '__main__':
    if len(argv) != 2:
        print(f"Usage {argv[0]} PID")
    else:
        main(int(argv[1]))
