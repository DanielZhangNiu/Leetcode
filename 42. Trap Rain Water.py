
"""
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
    
    
    The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
    
    Example:
    
    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    
"""
def trap(self, height):
    if not height: return 0
    left, right = 0 , len(height)-1
    LH, RH = height[left], height[right]
    res = 0
    while left < right:
        if LH < RH:
            left += 1
            if LH > height[left]:
                res += LH - height[left]
            else:
                LH = height[left]
        else:
            right -= 1
            if RH > height[right]:
                res += RH - height[right]
            else:
                RH = height[right]

    return res
