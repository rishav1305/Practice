class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        res = set()

        for e in emails:
            temp_res = ''
            skip = False
            for i in range(len(e)):
                if e[i] == '@':
                    temp_res +=  e[i:]
                    break
                elif skip or e[i] == '.':
                    continue
                elif e[i] == '+':
                    skip = True
                    continue
                else:
                    temp_res += e[i]
            res.add(temp_res)
        
        return len(res)