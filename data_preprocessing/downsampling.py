import numpy as np
from pdb import set_trace as st
import csv

f = open('DataWsu.csv', 'r')
n = open('DataWsudown.csv', 'w')
i = 0

for line in f:
	# st()
	if i % 50 == 0:
		n.write(line)
	i = i + 1