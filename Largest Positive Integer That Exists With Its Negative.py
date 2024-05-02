class Solution:
    def findMaxK(self, nums: List[int]) -> int:        
        s_num = nums.sort()
        for i in nums:
            if 0-i in nums:
                return -i
        return -1