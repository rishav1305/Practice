class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]*len(arr)
        # prev = -1
        for i in range(len(arr)-1, 0, -1):
            res[i-1] = max(arr[i],  res[i])
            
            # print(i, arr[i], res)
        return res