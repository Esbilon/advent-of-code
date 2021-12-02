## Advent of Code 2021 - December 2
import numpy as np

test_data = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

def pos_change(list):
    x = np.array([0,0])
    for elem in list:
        [head,dis] = elem.split()
        if head == "forward":
            x += [int(dis),0]
        elif head == "down":
            x += [0,int(dis)]
        elif head == "up":
            x += [0,-int(dis)]
        prod = np.prod(x)
    return prod
pos_change(test_data)

with open("02dec-data.txt") as f:
    prob1_data = [line for line in f.readlines()]
pos_change(prob1_data)

def pos_change_aim(list):
    x = np.array([0,0,0])
    for elem in list:
        [head,dis] = elem.split()
        if head == "forward":
            x += [int(dis),int(dis)*x[2],0]
        elif head == "down":
            x += [0,0,int(dis)]
        elif head == "up":
            x += [0,0,-int(dis)]
#        print(x)
    prod = np.prod(x[0:2])
    return prod
pos_change_aim(test_data)
pos_change_aim(prob1_data)