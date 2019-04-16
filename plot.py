#!/usr/bin/env python3

import numpy as np
from pathlib import Path
from sys import argv

import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt

def main(infile, outfile):
    lines = [line for line in Path(infile).read_text().split('\n') if line.strip()]
    t, n, u = zip(*[tuple(float(x) for x in line.split()) for line in lines])
    dt = np.array([t1 - t0 for t1, t0 in zip(t[1:], t)])
    t = np.array(t).astype('datetime64[s]')
    n = np.array(n).astype('uint16')
    u = np.array(u) / 1e6

    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(12, 12))
    ax1.plot(t, u, 'b-')
    ax1.set_xlabel('Timestamp')
    ax1.set_ylabel('RSS (in MB)')

    ax2.plot(t, n, 'g.')
    ax2.set_xlabel('Timestamp')
    ax2.set_ylabel('Number of processes')

    ax3.plot(t[1:], dt, 'r.')
    ax3.set_xlabel('Timestamp')
    ax3.set_ylabel('Log delay (in seconds)')

    fig.tight_layout()
    fig.savefig(outfile)


if __name__ == '__main__':
    if len(argv) != 3:
        print(f"Usage {argv[0]} infile.txt outfile.png")
    else:
        infile = argv[1]
        outfile = argv[2]
        main(infile, outfile)
