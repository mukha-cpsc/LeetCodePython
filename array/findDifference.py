def findTheDifference(s: str, t: str) -> str:
    map1 = {}
    map2 = {}
    for char in s:
        map1[char] = map1.get(char, 0) + 1
    for char in t:
        map2[char] = map2.get(char, 0) + 1
        if (char in s):
            del(map2[char])
    key, item = map2.items()
    print(key, item)
    return key
s = "abcd"
t = "abcde"
print(findTheDifference(s, t))