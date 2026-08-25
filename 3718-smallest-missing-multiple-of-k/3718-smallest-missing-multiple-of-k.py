class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        for i in range(1,1000):
            if i % k ==0:
                if i not in a :
                    return i