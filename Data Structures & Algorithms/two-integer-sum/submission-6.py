class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i,v in enumerate(nums):
            for x,y in enumerate(nums):
                if y+v==target:
                    if i!=x:
                        output.append(i)
                        output.append(x)
                        return(output)