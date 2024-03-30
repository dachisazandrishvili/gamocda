def word(word):
    snts = ""
    for char in word:
        if word.count(char) == 1:
            snts+= "("         
                 
        else:
            snts += ")"
    print(snts)

word("toom")