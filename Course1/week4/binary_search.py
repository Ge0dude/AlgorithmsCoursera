# Uses python3
import sys

file = open('/Users/brendontucker/AlgorithmsCoursera/Course1/week4/binarySearchTest1')
sys.stdin = file

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(linear_search(a, x), end = ' ')
