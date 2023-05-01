'''
Merging function
'''
def merge(left, right):
    result = [] # empty container to store the sorted elements
    i = j = 0 # 2 variables acting as points for each sub-arrays

    while i<len(left) and j<len(right): #looping thru the subarrays
        if left[i] < right[j]: 
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    result += left[i:]
    result += right[j:]
    return result

'''
Divide and sorting function
'''
def sorting(arr):
    if len(arr) <= 1:
        return arr
    
    #Dividing the arr into 2 sub-arrays
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    #Recursively sorting the subarrays
    sortingLeft = sorting(left) # sorting the left sub-array
    sortingRight = sorting(right) # soritng the right sub-array

    #merging the sub-arrays into a sorted array
    return merge(sortingLeft,sortingRight)

arr = [3, 7, 2, 9, 1, 6, 8, 5]
print(sorting(arr))