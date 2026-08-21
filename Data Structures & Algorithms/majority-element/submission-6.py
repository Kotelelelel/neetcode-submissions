class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for i in nums:
            if i == res:
                count += 1
            else:
                if count == 0:
                    res = i
                    count = 1
                count -= 1
                
        
        return res