class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for x, letter in enumerate(strs[0]):
            match = True
            for z in strs:
                if x >= len(z) or z[x] != letter:
                    match = False
                    break           
            if match:
                prefix = prefix + letter
            else:
                break
        return prefix
