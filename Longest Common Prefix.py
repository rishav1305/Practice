class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(res)):
                print(i, j, res, strs[i], res[j])
                if j>=len(strs[i]) or res[j] != strs[i][j]:
                    res = res[:j]
                    break
        return res
            



