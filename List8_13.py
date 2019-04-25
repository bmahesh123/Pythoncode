class List8:

    def longer_word(n, str):
        word_len = []
        txt = str.split(" ")

        for x in txt:
            if len(x) > n:
                word_len.append(x)
        return word_len

    print(longer_word(5, "This is world of python You need to update yourself"))