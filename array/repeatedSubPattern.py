class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern = ""
        for char in s:
            pattern += char
            if (pattern * (len(s) // len(pattern)) == s and len(pattern) != len(s)):
                #print(pattern * (len(s) // len(pattern)))
                return True
        return False
s = "abcabcabcabc"
print(Solution().repeatedSubstringPattern(s))