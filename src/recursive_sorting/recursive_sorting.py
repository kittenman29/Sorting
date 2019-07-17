"""
5 1 9 3 7 2 8 4
5 1 9 3        7 2 8 4
5 1       9 3        7 2     8 4
5   1    9   3     7     2    8    4

[1 5] [3 9] [2 7] [4 8]
[1 3 5 9] [2 4 7 8]
[1 2 3 4 5 7 8 9]
"""

def merge(l, r):
    a = 0
    b = 0

    result = []

    while len(l) > 0 and len(r) > 0:
        if l[0] < r[0]:
            v = l.pop(0)
        else:
            v = r.pop(0)
        
        result.append(v)

    result += l
    result += r

    return result

def mergesort(l):
    if len(l) <= 1:
        return l
    
    halfway_index = len(l)//2

    left = mergesort(l[:halfway_index])
    right = mergesort(l[halfway_index:])

    return merge(left, right)

print(mergesort([0]))
print(mergesort([2]))
print(mergesort([1,2]))
print(mergesort([2,1]))
print(mergesort([1,2,2,1]))
print(mergesort([1,2,3,4]))
print(mergesort([4,3,1,2]))
print(mergesort([4,3,2,1]))




# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    # TO-DO
    
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr











# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
