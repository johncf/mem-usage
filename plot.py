#!/usr/bin/env python3

import numpy as np
from pathlib import Path
from sys import argv

import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt

def main(infile, outfile):
    lines = [line for line in Path(infile).read_text().split('\n') if line.strip()]
    x, y = zip(*[tuple(float(x) for x in line.split()) for line in lines])
    plt.plot(np.array(x).astype('datetime64[s]'), np.array(y) / 1e6)
    plt.xlabel('Timestamp')
    plt.ylabel('RSS (in MB)')
    plt.savefig(outfile)


if __name__ == '__main__':
    if len(argv) != 3:
        print(f"Usage {argv[0]} infile.txt outfile.png")
    else:
        infile = argv[1]
        outfile = argv[2]
        main(infile, outfile)
