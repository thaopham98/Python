## This is like calculating the AREA of a RECTANGLE
## Width is the space between 2 indices, right - left
## Height is the SMALLEST value of 2 elements in the list
def maxArea(heights: int) -> int:
    width = 1
    left, right = 0, len(heights)-1
    max_area = 0
    while left<right:
        width = right - left
        area = width * min(heights[left], heights[right]) # formula: Width * Height
        # print(f"{width} * {min(heights[left], heights[right])} = {area}")

        if area > max_area: # only update the max_area when there is a larger area
            max_area = area

        if heights[left] < heights[right]:
            left += 1
        else:
            right-= 1
        
    return max_area

height = [1,7,2,5,4,7,3,6] # 36, height is 6, width is 6, the elements are [7,6]

result1 = maxArea(heights=height)
print('Max Area: ', result1)