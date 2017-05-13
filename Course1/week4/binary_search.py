# Uses python3
'''
changed x to b so that it matched the problem explanation
'''
import sys

file = open('/Users/brendontucker/AlgorithmsCoursera/Course1/week4/binarySearchTest1')
sys.stdin = file

def binary_search_recursive(list1, toFind, left=0, right=n):
#    if toFind > list1[-1]:
#        return -1
    if right < left:
        return -1
    print('left is:', left, 'right is:', right)
    mid = left + ((right - left)//2)
    print('this is mid:','[', mid, ']')
    if toFind == list1[mid]:
        print('number was found:', mid )
        return mid
    elif toFind < list1[mid]:
        #mid = mid - 1
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
        print(binary_search_recursive(a, b), end = ' ')
     
      
#def linear_search(a, b):
#    for i in range(len(a)):
#        if a[i] == b:
#            return i
#    return -1



#
#def binary_search(listA, toFind):
#    left, right = 0, len(a) - 1
#    # write your code here
#    low = listA[left]
#    print(low)
#    high = listA[right]
#    print(high)
#    if toFind > high:
#        return -1
#    elif toFind < low:
#        return -1
#    else:
#        mid = left + ((right - left) // 2)
#        print(mid)
#        if a[mid] == b:
#            return mid
#        elif b < a[mid]:
#            return binary_search(listA[:mid], toFind)
#        elif b > a[mid]:
#            return binary_search(listA[:right], toFind)


#def binary_search(listA, toFind, left=0, right=1):
#    left, right = 0, len(a) - 1
#    # write your code here
#    low = listA[left]
#    print(low)
#    high = listA[right]
#    print(high)
#    if toFind > high:
#        return -1
#    elif toFind < low:
#        return -1
#    else:
#        mid = left + ((right - left) // 2)
#        print(mid)
#        if a[mid] == b:
#            return mid
#        elif b < a[mid]:
#            return binary_search(listA, toFind, left, mid)
#        elif b > a[mid]:
#            return binary_search(listA, toFind, mid, right)

#def binary_search_recursive(list1, toFind):
#    if len(list1) == 0:
#        return -1
#    elif toFind < list1[0]:
#        return -1
#    elif toFind > list1[len(list1) -1]:
#        return -1
#    else:
#        mid = len(list1)//2
#        if toFind == list1[mid]:
#            return mid
#        elif toFind > list1[mid]:
#            return binary_search_recursive(list1[mid+1:], toFind)
#        else:
#            return binary_search_recursive(list1[:mid], toFind)


#
#def binary_search_recursive(list1, toFind, left=0, right=None): #could do n-1
#    left = left
#    if type(right) == None:
#        right = len(list1) - 1
#    else:
#        right = len(list1[left:right]) 
#    if len(list1) == 0:
#        return -1
#    elif toFind < list1[0]:
#        return -1
#    elif toFind > list1[len(list1) -1]:
#        return -1
#    else:
#        mid = left + ((right - left) // 2)
#        if toFind == list1[mid]:
#            return mid
#        elif toFind > list1[mid]:
#            return binary_search_recursive(list1, toFind, mid + 1, right)
#        else:
#            return binary_search_recursive(list1, toFind, left, mid  - 1)