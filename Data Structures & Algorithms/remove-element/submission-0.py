class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        while True:
            if val in nums:
                nums.remove(val)
            else:
                break
        return(len(nums))