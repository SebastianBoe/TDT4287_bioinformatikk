#!/usr/bin/python

from os import *
import sys
from collections import defaultdict

lines = [int(line) for line in sys.stdin.readlines()]
lengths = defaultdict(int)

print("Sequences with some prefix-suffix match: " + str(len([line for line in lines if line != 76])))

for line in lines:
	lengths[line] += 1

import numpy as np
import matplotlib.pyplot as plt

# Generate data...
x = lengths.keys()
y = lengths.values()

# Plot...
plt.scatter(x, y, c=y, s=2)
plt.gray()

plt.show()
