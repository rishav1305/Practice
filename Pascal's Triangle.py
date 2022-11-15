class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            print(i, res)
            lst = [0] + res[-1] + [0]
            temp_res = []
            for i in range(len(lst)-1):
                temp_res.append(lst[i]+lst[i+1])
            
            res += [temp_res]
        return res

