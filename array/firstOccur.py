class Solution:


    def strStr(haystack: str, needle: str) -> int:
        if (len(needle) == 0):
            return -1
        if (len(needle) > len(haystack)):
            return -1
        result = -1
        j = 0
        flag = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[j]:
                if flag == 0:
                    result = i
                    flag = 1
                j += 1
            else:
                result = -1
            if (j == len(needle)):
                return result
        return result


haystack = "mississippi"
needle = "issip"
print(Solution.strStr(haystack, needle))
