class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def firstCal(s, t):    
            hashmap = {}
            for i in range(len(s)):
                if s[i] not in hashmap.keys():
                    hashmap[s[i]] = t[i]
                elif hashmap[s[i]] != t[i]:
                    return False
                else:
                    continue
                
            return True
        
        return firstCal(s, t) and firstCal(t, s)
                