class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for e in emails:
            e1 = e.split('@')
            res.add('@'.join([e1[0].replace('.', '').split('+')[0], e1[1]]))

        return len(res)