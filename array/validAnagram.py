class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for char in s:
            map[char] = map.get(char, 0) + 1
        for char in t:
            map[char] = map.get(char, 0) - 1
        for key, value in map.items():
            if value != 0:
                return False
        return True
s = "rat"
t = "car"
print(Solution().isAnagram(s, t))