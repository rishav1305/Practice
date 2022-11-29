class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {'a':1, 'b': 1, 'l':2, 'n':1, 'o':2}
        hashmap = {}
        for i in text:
            hashmap[i] = hashmap.get(i, 0) + 1

        res = float('inf')

        for key in balloon.keys():
            res = min(res, hashmap.get(key, 0)//balloon[key])
        
        return res
