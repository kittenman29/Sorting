def linear_search(array, data):
    # loop through the array
    for item in array:
        # check if item matches the parameter
        if item == data:
            return item
    return f"that item isn't in the array"

print(linear_search([1, 3, 4, 5, 6, 7, 8], 4))



def binary_search(array, data):
    left = 0
    right = len(array) - 1
    done = False

    # if the data point is in the array
    while left<=right and not done:
        # define the midpoint of the array
        mid = (left+right)//2
        # if the midpoint is the data point, return true
        if array[mid] == data:
            done = True
        else:
            # if the midpoint is more than your data point
            if array[mid] > data:
                # return an array with only the numbers less than midpoint
                right = right -1
            else:
                # return an array with only the numbers more than midpoint
                left = left + 1
    return done

print(binary_search([2, 5, 6, 8, 9, 11, 14, 16], 58934))
            
