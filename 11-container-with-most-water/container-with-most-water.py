class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxWater =0
        while left<right:
            length = min(height[left],height[right])
            width = right-left
            result = length*width
            maxWater = max(result,maxWater)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxWater