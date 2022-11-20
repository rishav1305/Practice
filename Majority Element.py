class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        for k, v in hashmap.items():
            if v > len(nums)  // 2:
                return k
