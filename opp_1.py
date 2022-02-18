ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
VOVELS = 'aeiouy'
CONSTANTS = 'bcdfghjklmnpqrstvwxz'
WEIGHT = dict(zip(list(ALPHABET), list(range(1, len(ALPHABET) + 1))))


class SomeClass():

    def __init__(self, word):
        self.word = word

    def decision(self):
        '''
        Функция возвращает:
        - Если строка:
        если произведение гласных и согласных букв меньше или
        равно длине слова, выводить все гласные, иначе согласные;
        - Если число:
        произведение суммы чётных цифр на длину числа.
        '''
        vovels = []
        constants = []
        mult_string = 1
        if isinstance(self.word, str):
            for el in self.word.lower():
                for k, v in WEIGHT.items():
                    if el == k:
                        mult_string *= v
                        if el in VOVELS:
                            vovels.append(el)
                        if el in CONSTANTS:
                            constants.append(el)

            if mult_string <= len(self.word):
                return vovels
            else:
                return constants

        if isinstance(self.word, int):
            even_numbers_sum = sum([int(i) for i in list(str(self.word)) if not int(i) % 2])
            return even_numbers_sum


obj = SomeClass(123)
print(obj.decision())