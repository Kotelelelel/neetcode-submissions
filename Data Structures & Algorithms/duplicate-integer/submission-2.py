class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dis = list(set(nums))
        if len(dis) == len(nums):
            return False
        else:
            return True