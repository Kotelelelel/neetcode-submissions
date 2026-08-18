class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            if x in d:
                d[x] +=1
            else:
                d[x] = 1
        list_from_dic = sorted(list(d.items()),key=lambda x: x[1])
        return(list_from_dic[-1][0])
        