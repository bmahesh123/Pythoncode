class List4:

    def match_string(in_string):
        ctr = 0

        for string in in_string:
            if len(string) > 1 and string[0] == string[-1]:
                ctr = ctr + 1
        return ctr

    print(match_string(['sirs', '2ef12', 'yzx', 'aba', '1221']))

