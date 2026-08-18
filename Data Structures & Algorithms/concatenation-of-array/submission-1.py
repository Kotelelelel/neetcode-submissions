class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        x = 0
        while x<length:
            nums.append(nums[x])
            x+=1
        return(nums)