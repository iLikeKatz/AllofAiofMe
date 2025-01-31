import random
from timeit import default_timer as timer
def merge_sort(list):
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)

def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l


list = random.sample(range(0,10000), 10000)
start = timer()
result = merge_sort(list)
end = timer()
print(end-start, "sec")

"""
1k : 0.0017884659973788075 sec
10k : 0.02331554200281971 sec

time : O(n log n)
space : O(n)
"""