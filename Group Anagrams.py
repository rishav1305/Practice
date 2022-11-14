class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
                
        for s in strs:
            key = [0]*26
            for c in s:
                diff = ord(c) - ord('a')
                key[diff] += 1
            hashmap[tuple(key)].append(s)
        
            
        return hashmap.values()
        
        