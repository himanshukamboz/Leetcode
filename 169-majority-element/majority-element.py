class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        number=0
        for num in nums:
            if count==0:
                number=num
                count+=1
            elif num!=number:
                count-=1
            else:
                count+=1    
        return number


