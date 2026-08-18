class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()
        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x] = 1
        arr = []
        for num, appearances in dic.items():
            arr.append([appearances, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return(res)


            