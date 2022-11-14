class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)
        
        l, r = 0, 1
        res = 0
        while l < r and r < len(s):
            
            # print(l, r, s[l:r], res, end=' => ')
            
            if s[r] == s[r-1]:
                l = r
                r += 1
                res = max(res, r - l)
                continue
            
            if s[r] in s[l:r]:
                l += 1
            else:
                r += 1
            
            res = max(res, r - l)
            # print(l, r, s[l:r], res)

        return res
    
            # if s[r] == s[r-1]:
            #     l = r
            #     r += 1
            # elif s[l] == s[r]:
            #     l += 1
            # else:
            #     r += 1
            