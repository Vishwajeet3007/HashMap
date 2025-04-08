def replaceWord(dictionary , sentence):
    root_set = set(dictionary)
    def replace(word):
        for i in range(1,len(word) + 1):
            if word[:i] in root_set:
                return word[:i]
        return word
    return " ".join(replace(word) for word in sentence.split())
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(replaceWord(dictionary,sentence))

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(replaceWord(dictionary,sentence))
