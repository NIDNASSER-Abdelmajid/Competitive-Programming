class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            closest = nums[0]
            n = len(nums)
            for i in range(1,n):
                ref = nums[i]
                if abs(closest) > abs(ref):
                    closest = ref
                elif abs(closest) == abs(ref):
                    closest = max(closest, ref)
            return closest

