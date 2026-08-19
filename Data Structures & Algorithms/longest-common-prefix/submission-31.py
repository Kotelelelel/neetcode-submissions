class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        element = strs[0]
        prefix = []

        for x in range(len(element)):
            for y in range(len(strs)):
                if x >= len(strs[y]):
                    return(''.join(prefix))
                if element[x] != strs[y][x]:
                    return(''.join(prefix))
            prefix.append(element[x])
        return(''.join(prefix))
            
