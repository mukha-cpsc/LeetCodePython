class Solution:
    def strStr(haystack: str, needle: str) -> int:
        haystack_pointer = 0
        needle_pointer = 0
        if (len(needle) > len(haystack)):
            return -1
        if (len(needle) == 0):
            return 0
        while haystack_pointer < len(haystack):
            if haystack[haystack_pointer] == needle[needle_pointer]:
                haystack_pointer += 1
                needle_pointer += 1
            else:
                haystack_pointer = haystack_pointer - needle_pointer + 1
                needle_pointer = 0
            if needle_pointer == len(needle):
                return haystack_pointer - needle_pointer
        return -1
haystack = "mississippi"
needle = "issip"
print(Solution.strStr(haystack, needle))
