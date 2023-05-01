def rotate( nums, k) :
        """
        Do not return anything, modify nums in-place instead.
        """
        #queue
        # for i in range(k):
        #     # print(f'nums[i]: {nums[i]} at i: {i}')
        #     tempt = nums.pop(0)
        #     nums.append(tempt)
        #     print(nums)

        #stack
        # last = len(nums) - 1
        # for i in range(k):
        #     first = nums.pop(last)
        #     nums.insert(0,first)
        #     print(nums)

        nums.reverse()
        for i in range(k):
            num = nums.pop(0)
            nums.append(num)
        nums.reverse()
        print(nums)

n = [1,2,3,4,5,6,7]
#    0,1,2,3,4,5,6
rotate(n, 2)