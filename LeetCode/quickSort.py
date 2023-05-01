array = [2,1,0,5,8,7,6,3]

"""Partition"""
# def partition(array, leftP, rightP):
#     # Choosing the right-most element as the pivot
#     # pivot_position = rightP # Assignment the value of the right-most element to pivot
#     pivot = array[rightP] # Assigning the position of the right-most element to pivot

#     # print(f'Pivot position value: {pivot_position}')
#     print(f'Pivot: {pivot}')

#     i = leftP + 1 
#     j = rightP - 1 

#     print(i)
#     print(j)

#     print(f'Value of Right pointer: {rightP}')
#     print(f'Value of Left pointer: {leftP}')

#     print(array)
#     print(f'Array length: {len(array)}')


"""Quick Sort"""


def partition(array, low, high):
  
    # Choose the rightmost element as pivot
    pivot = array[high]
    print(f'Making Pivot the right-most element: {pivot}')
  
    # Pointer for greater element
    i = low - 1
    print(f'i: {i}')
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            print(f'Element <= pivot')
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            print(f'Updating i: {i}')
            print(f'Array[i]: {array[i]}')
            print(f'Array[j]: {array[j]}')
  
            # Swapping element at i with element at j
            print(f'Start to swap 2 elements.')
            (array[i], array[j]) = (array[j], array[i])
            print(f'Finish swapping 2 elements.')
  
    # Swap the pivot element with 
    # e greater element specified by i
    print(f'++Start to swap 2 elements')
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    print(f'++Finish swapping 2 elements.')
    # Return the position from where partition is done
    return i + 1

partition(array, 0, len(array)-1)
