ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
VOVELS = 'aeiouy'
CONSONANS = 'bcdfghjklmnpqrstvwxz'
WEIGHT = dict(zip(list(ALPHABET), list(range(1, len(ALPHABET) + 1))))


class SomeClass():

    def __init__(self, word):
        self.word = word

    def is_type(self):
        '''
        Accepts an object. Returns its type.
        '''
        return type(self.word)

    def method_str(self):
        '''
        Takes a string. returns the vowels of the string
        if the multiplication of the letters of the string
        is less than the length of the string.
        Else returns the consonants of the string.
        '''
        vovels = []
        consonants = []
        mult_string = 1
        for el in self.word.lower():
            for k, v in WEIGHT.items():
                if el == k:
                    mult_string *= v
                    if el in VOVELS:
                        vovels.append(el)
                    if el in CONSONANS:
                        consonants.append(el)
        if mult_string <= len(self.word):
            return vovels
        else:
            return consonants

    def method_int(self):
        """
        Takes a number. Returns the sum of the even digits of a number
        """
        even_numbers_sum = sum([int(i) for i in list(str(self.word)) if not int(i) % 2])
        return even_numbers_sum


obj = SomeClass('spam')
method = obj.is_type()
if method == str:
    print(obj.method_str())
elif method == int:
    print(obj.method_int())
else:
    print('Unsupported type!')
