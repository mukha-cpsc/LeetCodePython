class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_count = 0
        for elem in arr:
            if elem == 0:
                zero_count += 1
        if zero_count == 0:
            return arr
        for i in range(len(arr)):
            print(arr)
            if arr[i] == 0:
                for j in range(len(arr) - 1, i + 1, -1):
                    arr[j] = arr[j - 1]
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                arr[i] = 0
        return arr
arr = [0,4,1,0,0,8,0,0,3]
print(Solution.duplicateZeros(Solution(), arr))