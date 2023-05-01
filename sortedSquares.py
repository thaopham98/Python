from typing import List
class Solution:
    # def bubbleSort(self, list: List[int])-> List[int]:
    #         n = len(list)
    #         for i in range(n - 1):
    #             for j in range(0, n-i-1):
    #                 if list[j] > list[j+1]:
    #                     list[j], list[j+1] = list[j+1], list[j]

    #         return list        


    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    
        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
    
        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]
    
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
    
        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
    
        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    
    # l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
    def mergeSort(self, arr, l, r):
        if l < r:
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l+(r-l)//2
            # print(f"m: {m}")
    
            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r)
        
        return arr

    

    def sortedSquares(self, nums: List[int]) -> List[int]:
        list = []
        i = 0
        while i < len(nums):
            e = nums[i] ** 2
            list.append(e)
            i += 1
        # sorting = self.bubbleSort(list)
        # return sorting
        low = 0
        high = len(list)
        mergeSort1 = self.mergeSort(list, low, high-1)
        # print(f'Merge Sorting 1: {mergeSort1}')
        return mergeSort1
        # return sorted(list)

      
            
# nums = [-4,-1,0,3,10]
test1=Solution()
print(test1.sortedSquares([-4,-1,0,3,10]))
