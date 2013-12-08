
import sys
from collections import defaultdict
from os import *

adapter = sys.argv[1]
lines = [int(line) for line in sys.stdin.readlines()]

j = []
for line in

print("Sequences with some prefix-suffix match: " + str(len([line for line in lines if line != 50])))

lengths = defaultdict(int)
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
