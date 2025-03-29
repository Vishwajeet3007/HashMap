def wordPattern(pattern,sentence):
    tokens = sentence.split()
    if len(tokens) != len(pattern):
        return False
    word_to_char = {}
    char_to_word = {}
    for ch , word in zip(pattern,tokens):
        if word in word_to_char and word_to_char[word] != ch:
            return False
        if ch in char_to_word and char_to_word[ch] != word:
            return False
        word_to_char[word] = ch
        char_to_word[ch] = word
    return True
pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern,s))
pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern,s))