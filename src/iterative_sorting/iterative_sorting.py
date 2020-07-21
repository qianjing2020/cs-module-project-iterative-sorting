# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        min_idx = arr.index(min(arr[i:]))
        # swap
        a = arr[min_idx]
        arr[min_idx] = arr[smallest_index]
        arr[smallest_index] = a

    return arr

import random   
array = list(range(0, 9))
random.shuffle(array)
print(array)
print(selection_sort(array))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # make a series of swaps between adjacent elements, gradually moving larger elements towards the end of the array (or bubbling larger elements up)
    # loop through n-1 elements
    arr_index = list(range(0, len(arr)))
    end_sort_index = arr_index[-1::-1] 
    for end_sort in end_sort_index:
        for i in range(0, end_sort):
                    
            # if current index value is bigger, bubble toward right     
            if arr[i] > arr[i+1]:
                # swap
                a = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = a

    return arr


random.shuffle(array)
print(array)
print(bubble_sort(array))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    if maximum == None:
        maximum = max(arr)
    # create count list to store count value 
    output = [0 for i in range(maximum)] 
    # to store the result sorted array
    result = [i for i in arr]  
    count_idx = list(range(maximum))
    count_lst = [0 for i in range(maximum)]
    # count count_idx appearance in array and store the counts in corresponding count_lst
    for i in count_idx:
        count_lst[i] = arr.count(i)
    # modify count by adding its previous count
    for i in count_idx[:-1]:
        count_lst[i+1] += count_lst[i]
    
    # Build the output count array
    for i in range(len(arr)):
        output[count_lst[(arr[i])]-1] = arr[i]
        count_lst[arr[i]] -= 1
    
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        result[i] = output[i]
    return result
    

random.shuffle(array)
print(array)
print(counting_sort(array))
