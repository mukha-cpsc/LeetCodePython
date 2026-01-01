class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        res = []
        for i, x in enumerate(nums):
            rest = nums[:i] + nums[i + 1:]
            for p in Solution.permute(Solution(), rest):
                res.append([x] + p)
        return res
nums = [1, 2, 3]
print(Solution.permute(Solution(), nums))