class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        freq = [[] for x in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for n, m in count.items():
            freq[m].append(n)
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                return n