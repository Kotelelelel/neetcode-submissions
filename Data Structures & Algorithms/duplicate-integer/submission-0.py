class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = []
        for x in nums:
            if x in copy:
                return True
            else:
                copy.append(x)
        return False