class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        for j in range(k+1,len(nums)):
            if nums[j]!=nums[k]:
                k+=1
                nums[k],nums[j]=nums[j],nums[k]
        return k+1