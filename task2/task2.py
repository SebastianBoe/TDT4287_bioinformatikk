
from math import *

MISMATCH_RATIO = 0.25
LINE_LENGTH = 50

stub = open('../task1/stub.txt', 'r')

f = open('../task1/adapter.txt', 'r')
adapter = f.read()[:-1]
f.close()

def difference(s1, s2, errors_allowed):
    return difference(s1[1:], s2[1:], errors_allowed - int(s1[0] != s2[0])) if ( s1 and s2 and errors_allowed >= 0) else errors_allowed 
    
for line in stub:
    line = line[:-1] #remove \n
    l = 50
    for i in range(len(line)):
        errors_allowed = floor(MISMATCH_RATIO * (LINE_LENGTH - i))
        if difference(line[i:], adapter[i:], errors_allowed) >= 0:
            # print remaining sequence length
            l = i
            break
    
    print(l)

stub.close()
