def strStr(haystack: str, needle: str) -> int:
    result = -1
    j = 0
    flag = 0
    for char in haystack:
        if char == needle[j]:
            if flag == 0:
                result = j
                flag = 1
            j += 1
        else:
            result = -1
        if (j == len(needle)):
            return result
    return result
haystack = "leetcode"
needle = "leet"
print(strStr(haystack, needle))
