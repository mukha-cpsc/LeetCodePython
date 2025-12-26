class Solution:
    def plusOne(self, digits):
        inital = digits.copy()
        n = len(digits)
        remains = (digits[n - 1] + 1) // 10
        #print(remains)
        if remains == 0:
            digits[n - 1] = digits[n - 1] + 1
            return digits
        else:
            digits[n - 1] = 0
            for i in range(n - 2, -1, -1):
                if (digits[i] + remains != 10):
                    digits[i] += remains
                    ##remains = digits[i] // 10
                else:
                    digits[i] = 0
                    remains = 1
        if Solution.allNines(inital):
            digits.append(0)
            digits[0] = 1
        return digits
    def allNines(self, digits):
        for elem in digits:
            if elem != 9:
                return False
        return True
digits = [9,9]
print(Solution.plusOne(Solution(), digits))