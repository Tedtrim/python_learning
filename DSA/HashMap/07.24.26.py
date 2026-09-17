word1 = "aab"
word2 = "abb"

def anagram_checker(word1, word2):
    chars1 = {}

    for char in word1:
        if char in chars1:
            chars1[char] += 1
        else:
            chars1[char] = 1

    for char in word2:
        if char in chars1:
            chars1[char] -= 1
        else:
            chars1[char] = -1

    return all(count == 0 for count in chars1.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

def anagram_grouper(words):
    anagrams = {}

    for word in words:
        key = "".join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)

    return list(anagrams.values())

print(anagram_grouper(["eat", "tea", "bat"]))


    