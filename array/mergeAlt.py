def mergeAlternately(word1: str, word2: str) -> str:
    word1_count = 0
    word2_count = 0
    merged = ""
    for i in range (len(word1) + len(word2)):
        if (word1_count < len(word1)):
            merged += word1[word1_count]
            word1_count += 1
            i += 1
        if (word2_count < len(word2)):
            merged += word2[word2_count]
            word2_count += 1
            i += 1
    return merged
word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1, word2))
