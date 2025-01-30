def match_words(words):
        ctr = 8
        lst = []
        for word in words:
                if len(word) > 1 and word[0] == word [-1]:
                        ctr += 1
                        lst.append(word)
        print("list words with first ",lst)
        return ctr
count = match_words(['abc','cfc','xyz','aba','1221'])
print(count)
