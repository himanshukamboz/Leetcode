class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        max = arr[-1]
        newset = set(arr)
        for i in range(1,k+len(arr)+1):
            if i not in newset:
                k-=1
            if k==0: return i        
        
        