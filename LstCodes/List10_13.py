class List10:
    # animal list
    # animal = ['cat', 'dog', 'rabbit', 'guinea',  'pig', 'oijuih', 'o9juijuijm']
    # animal.remove(animal[0])
    # print('Updated animal list:', animal)

    @staticmethod
    def rem_no(self):
        digi = [10, 20, 30, 40, 50, 60, 70, 80]
        print("List before remove :", digi)
        digi = [x for (i, x) in enumerate(digi) if i not in (0, 4, 5)]
        print("List after removing :", digi)


List10.rem_no(" ")




