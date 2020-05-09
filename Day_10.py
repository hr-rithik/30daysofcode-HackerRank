#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    num = bin(n).replace("0b","")
    count = 0
    prev = num[0]
    cnt = []
    for i in range(1, len(num)):
        if num[i] == "1": 
            if prev == num[i]:
                count += 1
        else:
            count = 0
        cnt.append(count+1)
        prev = num[i]
    print(max(cnt))
    