class Solution:
    def subsets(self, nums):
        if nums == None:
            return []
        if len(nums) == 1:
            return [[], [nums[0]]]
        head = nums[0]
        tail = nums[1:]
        subsets_tail = Solution.subsets(Solution(), tail)
        return subsets_tail + [[head] + list for list in subsets_tail]
arr = [1, 2, 3]
print(Solution.subsets(Solution(), arr))
