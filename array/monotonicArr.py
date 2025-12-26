class Solution:
    def isMonotonic(self, nums) -> bool:
        return Solution.onlyIncreasing(nums) or Solution.onlyDecreasing(nums)
    def onlyIncreasing(self, nums):
        for i in range(len(nums) - 1):
            if (nums[i + 1] < nums[i]):
                return False
        return True
    def onlyDecreasing(self, nums):
        for i in range(len(nums) - 1):
            if (nums[i + 1] > nums[i]):
                return False
        return True
arr = [1, 3, 2]
print(Solution.isMonotonic(arr))