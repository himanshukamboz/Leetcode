class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        text = str(abs(x))
        reversedNum = text[::-1]   
        rev = int(reversedNum)
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        if x<0:
            return rev*-1    
        return rev
