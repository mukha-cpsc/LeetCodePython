def findTheDifference(s: str, t: str) -> str:
    map1 = {}
    map2 = {}
    if (s == ""):
        return t
    for char in s:
        map1[char] = map1.get(char, 0) + 1
    for char in t:
        map2[char] = map2.get(char, 0) + 1
    #print(map1, map2)
    #print(map1, map2)
    for key, value in map2.items():
        if value > map1.get(key, 0):
            return key
    #print(map1, map2)
s = "abcd"
t = "abcde"
print(findTheDifference(s, t))