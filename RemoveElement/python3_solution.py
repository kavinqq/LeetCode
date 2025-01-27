from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        題目理解: 移除掉val元素後, 剩下的元素有幾個\
        """
        
        while val in nums:
            nums.remove(val)
            
        return len(nums)
        