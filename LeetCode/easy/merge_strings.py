def mergeAlternately(word1, word2):
        word = []
        for i in range(len(word1+word2)):
            if i < len(word1) and i < len(word2):
                word.append(word1[i])
                word.append(word2[i])
            else:
                if i < len(word1):
                    word.append(word1[i])
                elif i<len(word2):
                    word.append(word2[i])

        return "".join(word)


print(mergeAlternately("be", "bab"))
