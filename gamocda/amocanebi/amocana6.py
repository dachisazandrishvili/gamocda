def word(word):
    for char in word:
        if word.count(char) == 1:
            return char
            break     
        else:
            return "mgeli200"
            break

word("toom")