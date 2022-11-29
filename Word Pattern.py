class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split(' ')

        if len(s_split) != len(pattern):
            return False

        hashmap = {}
        for i in range(len(pattern)):
            if pattern[i] in hashmap.keys():
                if hashmap[pattern[i]] != s_split[i]:
                    return False
            else:
                hashmap[pattern[i]] = s_split[i]
        
        return True if len(set(hashmap.values())) == len(hashmap.values()) else False