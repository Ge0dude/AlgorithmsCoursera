#python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

first = 0
second = 0
for x in range(0, n):
    if a[x] > first:
        second = first
        first = a[x]
    elif a[x] > second:
        second = a[x]
        
result = first * second
print(result) 