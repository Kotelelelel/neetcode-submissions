class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            if "".join(sorted(i)) not in anagrams:
                anagrams["".join(sorted(i))] = [i]
            else:
                anagrams["".join(sorted(i))].append(i)

        ans = []
        for x in anagrams.values():
            ans.append(x)
        return ans