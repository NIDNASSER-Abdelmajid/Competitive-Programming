class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        nums = [0, *nums, 0]
        n = len(nums)
        for i in range(n-2):
            if sum(nums[:i+1]) == sum(nums[i+2:]):
                return i
        return -1