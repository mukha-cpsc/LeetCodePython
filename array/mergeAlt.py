def mergeAlternately(self, word1: str, word2: str) -> str:
    word1_count = 0
    word2_count = 0
    merged = ""
    while (word1_count < len(word1) and word2_count < len(word2)):
        merged.append(word1[word1_count])
        merged.append(word2[word2_count])
        word1_count += 1
        word2_count += 1
    return merged
