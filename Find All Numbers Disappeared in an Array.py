class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        mem = [False]*(len(nums))
        for i in nums:
            mem[i-1] = True

        res = []
        for i in range(len(mem)):
            if not mem[i]:
                res.append(i+1)
                
        return res