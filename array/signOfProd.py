class Solution:
    def arraySign(self, nums) -> int:
        #count_positives = 0
        zero_flag = 0
        count_negatives = 0
        for elem in nums:
            if elem < 0:
                count_negatives += 1
            elif elem == 0:
                zero_flag = 1
        if (zero_flag == 1):
            return 0
        if (count_negatives % 2 == 0):
            return 1
        return -1