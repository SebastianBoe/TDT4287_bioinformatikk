#!/usr/bin/python

from collections import defaultdict

import time
from heapq import *

start = time.time()

LINES = 10 ** 6
LINE_LENGTH = 76
USE_LESS_LINES = False

def build_suffix_table():
    dic = {'A' : 1, 'C' : 2, 'G' : 3, 'T' : 4, 'N' : 5}
    exp = {i : 6 ** (75 - i) for i in range(75, -1, -1)}

    stub = open('stub2.txt', 'r')

    j = 0
    suffixes = defaultdict(int)
    for line in stub:
        j += 1
        if j == 100000 and USE_LESS_LINES:
            break
        
        h = 0
        for i in xrange(75, -1, -1):
            h += dic[line[i]] * exp[i]
            suffixes[h] += 1

    stub.close()
    print("time: " + str(time.time() - start))
    return suffixes

def walk_the_walk(count):
    global LINES, LINE_LENGTH

    print("Entering walk")
    
    class Node:
        def children(self):
            if self.length == 76:
                return []

            children = []
            
            for letter in range(1,6):
                child_state = self.state + letter * (6 ** self.length)
                child_count = count[child_state]
                if child_count == 0:
                    continue

                #update table
                table[LINE_LENGTH - (self.length + 1)] += child_count

                child = Node()
                
                child.length = self.length + 1
                child.state = child_state

                child.lower_bound = child_count + self.lower_bound
                
                children.append(child)

            for child in children:
                potential = (LINE_LENGTH - child.length) * LINES - sum(table[:LINE_LENGTH - child.length])
                child.upper_bound = child.lower_bound + potential

            return children

        def __cmp__(self, other):
            return other.upper_bound - self.upper_bound

        def __str__(self):
            return "length = " + str(self.length) + ", state = " + str(self.state) + ", lower_bound = " + str(self.lower_bound) + ", upper_bound = " + str(self.upper_bound)

    #Used characters so far
    #read during calculation of upper bound
    #updated at creation of new children
    table = [0] * LINE_LENGTH
    
    root = Node()
    root.length = 0
    root.state = 0
    root.lower_bound = 0
    root.upper_bound = LINE_LENGTH * LINES
    
    states = []
    heappush(states, root)

    best = root
    while states:
        state = heappop(states)
            
        children = state.children()

        if children:
            #Update the best state, wrt. lower_bound
            lower, best = max(max([(child.lower_bound, child) for child in children]), (root.lower_bound, root))

            for child in children:
                #Prune children with upper bounds less than the globally lower bound
                if child.upper_bound >= lower:
                    heappush(states, child)

    return best

def decode(state):
    answer = ""
    while state:
        a = state % 6
        answer = "ACGTN"[a - 1] + answer
        state -= a
        state = state / 6
        
    return answer    

def main():
    best = walk_the_walk(build_suffix_table())
    print(best)
    s = best.state
    print(decode(s))

print("start")
main()
print("time: %f"%(time.time() - start))
print("end")
