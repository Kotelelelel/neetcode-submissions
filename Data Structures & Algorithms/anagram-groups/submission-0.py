class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for x in strs:
            sortedd = ''.join(sorted(x))
            output[sortedd].append(x)
        return list(output.values())