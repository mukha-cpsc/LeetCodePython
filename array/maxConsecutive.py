class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        mx = 0
        current = 0
        for elem in nums:
            if (elem == 1):
                current += 1
            elif (elem != 1):
                current = 0
            if (current > mx):
                mx = current
        return mx
arr = [1,0,1,1,0,1]
print(Solution.findMaxConsecutiveOnes(Solution(), arr))