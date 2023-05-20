import bisect
import collections
import copy
import heapq
import itertools
import math
import numpy
import string
import sys


def S(): return sys.stdin.readline().rstrip()


def I(): return int(sys.stdin.readline().rstrip())


def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


def LS(): return list(sys.stdin.readline().rstrip().split())


N = I()
A = [LI() for _ in range(N)]
