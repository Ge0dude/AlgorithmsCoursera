# Uses python3
'''
changed x to b so that it matched the problem explanation
'''
import sys

#file = open('/Users/brendontucker/AlgorithmsCoursera/Course1/week4/binarySearchTest2')
#sys.stdin = file

def binary_search_recursive(list1, toFind, left=0, right=1):
#    if toFind > list1[-1]:
#        return -1
    if right < left:
        return -1
    #print('left is:', left, 'right is:', right)
    mid = left + ((right - left)//2)
    if mid == len(list1):
        return - 1
    #print('this is mid:','[', mid, ']')
    if toFind == list1[mid]:
        #print('number was found:', mid )
        return mid
    elif toFind < list1[mid]:
        mid = mid - 1
        return binary_search_recursive(list1, toFind, left, mid)
    else:
        mid = mid + 1
        return binary_search_recursive(list1, toFind, mid, right)
    
    
 





            

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for b in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search_recursive(a, b, 0, n), end = ' ')
     
      
