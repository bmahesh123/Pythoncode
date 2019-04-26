import  operator


class Dict:

    @staticmethod
    def asds(self):
        dict = {}
        dic = {1: 'Hello', 2: 'Mahesh', 3: 'Python', 4: 'Developer'}
        # print("Empty Dic", dict)
        # print(dic)

        as_dic = sorted(dic.items(), key=operator.itemgetter(0))
        ds_dic = sorted(dic.items(), key=operator.itemgetter(0), reverse = True)
        print(as_dic)
        print(ds_dic)

    def adddict(self):
        dic = {}
        dic = {1: 'Hello', 2: 'Mahesh', 3: 'Python', 4: 'Developer'}
        # print("Empty Dic", dict)

        dic[5] = 'ML'
        dic[6] = 'AI'
        dic[7] = 'DL'

        print(dic)


    def concatdict(self):
        dic = {}
        dic = {1: 'Hello', 2: 'Mahesh', 3: 'Python', 4: 'Developer'}
        dic2 ={5: 'ML', 6: 'AI', 7: 'DL'}
        # print("Empty Dic", dict)
        dic.update(dic2)
        print(dic)
        # print(dic2)

    def concatdict(self):
        dic = {}
        dic = {1: 'Hello', 2: 'Mahesh', 3: 'Python', 4: 'Developer'}
        dic2 ={5: 'ML', 6: 'AI', 7: 'DL'}
        dic3 = {}
        # print("Empty Dic", dict)
        dic.update(dic2)

    def iterationdict(self):

        dic = {1: 'Hello', 2: 'Mahesh', 3: 'Python', 4: 'Developer'};
        for key,value in dic.items():

            print(key,value)

    def dictmultiplication_n(self):

        dict_num = int(input("Enter no to create Dict:"))
        d = dict()

        for m in range(1, dict_num + 1):
            d[m] = m * m
        print(d)



#Dict.asds(" ")
#Dict.adddict(" ")
#Dict.concatdict(" ")
#Dict.iterationdict(" ")
#Dict.dictmultiplication_n(" ")