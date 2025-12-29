class Solution:
    def findNumbers(self, nums) -> int:
        res = 0
        for elem in nums:
            if (Solution.digits(Solution(), elem) % 2 == 0):
                res += 1
        return res
    def digits(self, num):
        res = 0
        while (num >= 1):
            res += 1
            num = num / 10
        return res
num = 10
nums = [12,345,2,6,7896]
#print(Solution.digits(Solution(), num))
print(Solution.findNumbers(Solution(), nums))