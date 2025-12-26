class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        just_words = s.strip().split(" ")
        return(len(just_words[len(just_words) - 1]))
s = s = "Hello World"
print(Solution.lengthOfLastWord(Solution(), s))