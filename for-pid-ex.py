#!/usr/bin/env python3

import psutil
import random
import time
from sys import argv, stdout


def main(pid: int):
    """prints epoch-time, number of processes, RSS, VMS, USS, PSS, and swap (all in bytes) once every second"""
    # See http://grodola.blogspot.com/2016/02/psutil-4-real-process-memory-and-environ.html for USS, PSS
    p = psutil.Process(pid)
    while True:
        rss = get_rss(p)
        vms = get_vms(p)
        uss = get_prop(p, 'uss')
        pss = get_prop(p, 'pss')
        swap = get_prop(p, 'swap')
        if not rss:
            break
        num_proc = 1
        for c in p.children(True):
            rss += get_rss(c)
            vms += get_vms(c)
            uss += get_prop(c, 'uss')
            pss += get_prop(c, 'pss')
            swap += get_prop(c, 'swap')
            num_proc += 1
        print(f"{int(time.time())} {num_proc} {rss} {vms} {uss} {pss} {swap}")
        time.sleep(5)
        if random.randint(1, 20) == 1:
            stdout.flush()


def get_rss(proc):
    return get_prop(proc, 'rss')


def get_vms(proc):
    return get_prop(proc, 'vms')


def get_prop(proc, prop):
    try:
        return getattr(proc.memory_full_info(), prop, 0)
    except psutil.NoSuchProcess:
        return 0


if __name__ == '__main__':
    if len(argv) != 2:
        print(f"Usage {argv[0]} PID")
    else:
        main(int(argv[1]))
