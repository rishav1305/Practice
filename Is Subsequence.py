class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s=='':
            return True
        a = 0
        for i in t:
            if i == s[a]:
                a += 1
                if a == len(s):
                    return True
            
        return False