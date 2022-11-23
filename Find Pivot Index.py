class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)-1
        s = sum(nums)

        left = {0: 0}
        right = {l:0}

        for i in range(l):
            left[i+1] = left.get(i, 0) + nums[i]
            right[i] = right.get(i-1, s) - nums[i]

        for i in range(l+1):
            if left[i] == right[i]:
                return i
        return -1