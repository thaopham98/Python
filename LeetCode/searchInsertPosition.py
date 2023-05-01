def searchInsertPosition(list, target):
    l = 0
    h = len(list) -1

    while l<=h:
        m = l+((h-l)//2)
        print(f"m: {m}")

        # if l == h:
        #     print( f"target doesn't exist. m : {m}")
        #     if list[m] > target:
        #         print('i am here')
        #         return m
        #     elif list[m] < target:
        #         print("I am here 2")
        #         return m+1

        if list[m] == target:
            return m
        elif list[m] < target:
            l = m + 1
            print(f'Updating l: {l}')
        elif list[m] > target:
            h = m - 1
            print(f"Updating h: {h}")
    
    return l
        

test = searchInsertPosition([1,3,5,6], 5)
print(f"Result: {test}")