def add_in_end(string):
    for char in string:
        if int(string[-1]) is int:
            string.remove(string[-1])
            string + str(int(string[-1]) + 1)
        else:
            string + "l"
    return string
