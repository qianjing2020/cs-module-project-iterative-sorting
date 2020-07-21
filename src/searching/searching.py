import random
import time

def linear_search(arr, target):
    # given arr and target, return index of arr that arr[index]==target
    idx = 0 
    for item in arr:
        if item == target:
            return idx
        idx +=1    
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #Use binary search to return index of arr that arr[index]==target
    # first sort the array 
    lst_sorted = sorted(arr)
    # initialize start, end and midpoint for search
    start = 0
    end = len(lst_sorted) - 1 
    mid = (start+end)//2
    found = 0
    # while mid >1 and haven't found the target
    while mid >= 1 and found == 0:        
        # mid match target
        if target == lst_sorted[mid]:
            found = 1
            return mid
            
        # target is smaller than mid, search the left part   
        elif target < lst_sorted[mid]: 
            end = mid         
            
        elif target > lst_sorted[mid]:
            start = mid          

        mid = (start+end)//2
    return -1  # not found


lst = list(range(0, 100))
random.shuffle(lst)
target = 78
print(lst)
start_time = time.time()
print(linear_search(lst, target))
print(f'Runtime for linear search is {time.time()-start_time} seconds')


start_time = time.time()
print(binary_search(lst, target))
print(f'Runtime for binary search is {time.time()-start_time} seconds')
