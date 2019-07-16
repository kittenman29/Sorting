# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for u in range(len(arr)):
        min_index = u

        for s in range(u + 1, len(arr)):
            if arr[s] < arr[min_index]:
                min_index = s
        
        arr[u], arr[min_index] = arr[min_index], arr[u]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # loop through the array
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]        
    return arr
list = [4, 3, 2, 5, 1, 6]


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr