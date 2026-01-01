class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        subs = []
        Solution.allSubString(Solution(), s, 0, "", subs)
        for elem in subs[:]:
            if Solution.hasDuplicates(Solution(), elem) == True:
                print(elem)
                subs.remove(elem)
        mx = 0
        for arr in subs:
            if len(arr) > mx:
                mx = len(arr)
        return mx
    def allSubString(self, s, count, substr, res):
        #print(substr)
        if count == len(s):
            res.append(substr)
            return
        substr += s[count]

        Solution.allSubString(Solution(), s, count + 1, substr, res)

        substr = substr[:-1]

        Solution.allSubString(Solution(), s,count + 1, substr, res)
    def hasDuplicates(self, s):
        i = 1
        for char in s:
            if char in s[i:]:
                return True
            i += 1
        return False
str = "pwwkew"
print(Solution.lengthOfLongestSubstring(Solution(), str))