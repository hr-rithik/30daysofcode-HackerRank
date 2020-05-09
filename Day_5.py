#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    mul = 1
    for i in range(1, 11):
        mul = n * i
        print(n, "x", i, "=", mul)
