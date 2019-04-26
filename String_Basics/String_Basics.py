import textwrap


class String:
    @staticmethod
    def lenstring(self):
        string = "Hello"
        len_of_string = len(string)
        print(len_of_string)



    def occstring(self):

        print("Enter 'i' for interps excution.")
        string = input("Enter string:")
        if string == 'i':
            exit();
        else:
            char = input("Enter char to check occurrence:")
            val = string.count(char)
            print(char, "is occurred", val, "times")


    def change_string(str1):
        char = str1[0]
        str1 = str1.replace(char, '$')
        str1 = char + str1[1:]
        return str1
    # print(change_string('aheash'))


    def char_end_string(str3):
        length = len(str3)

        if length > 2:
            if str3[-3:] == 'ing':
                str3 += 'ly'
            else:
                str3 += 'ing'
        return str3
    # print(char_end_string('Hi'))
    # print(char_end_string('Hey'))
    # print(char_end_string('sing'))


    def find_long_string(list_of_words):
        len_of_word = []
        for x in list_of_words:
            len_of_word.append((len(x), x))
        len_of_word.sort()
        return len_of_word[-1][1]
    # print(find_long_string(["Java", "Net", "Python", "SpringH", "Hi"]))


    def upper_lower_string(list_of_words):
        string = input("Enter string:")
        print("String in Upper case:", string.upper())
        print("String in lower case:", string.lower())

    def uniqu_string_alpha(self):
        items = input("Enter Sequence of words:")
        words = [word for word in items.split(",")]
        print(",".join(sorted(list(set(words)))))

    def string_split(self):
        str1 = 'https://www.google.com/python-exercises/bridzlab/mnb'
        print(str1.rsplit('/', 1)[0])
        print(str1.rsplit('-', 1)[0])
        print(str1.rsplit('.', 1)[0])
        print(str1.rsplit('//', 1)[0])


    def disp_string_wid(self):
        string_text = '''
          In machine learning and pattern recognition,
          a feature is an individual measurable property or 
          characteristic of a phenomenon being observed. 
         '''
        print(textwrap.fill(string_text, width=50))


    def substring_occ(self):

        string_occ='This is Python world You need to wok hard then its not hard'
        print("Given string: ", string_occ)
        occ=string_occ.count('hard')
        print("occurrence of of word is:", occ)


# String.lenstring(" ")
# String.occstring(" ")
# String.change_string(" ")
# String.char_end_string(" ")
# String.find_long_string(" ")
# String.upper_lower_string(" ")
# String.uniqu_string_alpha(" ")
# String.string_split(" ")
# String.disp_string_wid("")
# String.substring_occ("")


