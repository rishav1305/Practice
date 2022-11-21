class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(nums2)):
            
            hashmap[nums2[i]] = -1
            
            for e in nums2[i:]:
                if e > nums2[i]:
                    hashmap[nums2[i]] = e
                    break
            
        res = []
        for n in nums1:
            res.append(hashmap[n])

        return res