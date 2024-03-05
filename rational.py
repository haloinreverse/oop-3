
class TRational:
    def __init__(self, *args):
        if isinstance(args, int):
            self.__num = args
            self.__denom = 1
        elif len(args) == 1:
            if '/' in args:
                self.__num = int(args.replace(' ', '').split('/')[0])
                self.__denom = int(args.replace(' ', '').split('/')[0])
            else:
                self.__num = int(args.replace(' ', ''))
                self.__denom = 1
        else:
            self.__num = args[0]
            self.__denom = args[1]


    def __eq__(self, other):
        if self.__num == other.__num and self.__denom == other.__denom:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __abs__(self):
        return TRational(abs(self.__num), self.__denom)

    def __str__(self):
        return f'{self.__num}/{self.__denom}'

    def __mul__(self, other):
        new_num = self.__num * other.__num
        new_denom = self.__denom * self.__denom
        return TRational(new_num, new_denom).__reduce()

    def __add__(self, other):
        return TRational(self.__num * other.__denom + other.__num * self.__denom, self.denom * other.__denom).__reduce()

    def __sub__(self, other):
        return TRational(self.__num * other.__denom - other.__num * self.__denom, self.denom * other.__denom).__reduce()

    def __truediv__(self, other):
        return TRational(self.__num * other.__denom, self.__denom * other.__num).__reduce()

    ## вспомогательный метод для поиска НОД (используется для сокращения дроби)
    def __nod(self):
        m, n = max(abs(self.__num), abs(self.__denom)), min(abs(self.__num), abs(self.__denom))
        while m != 0 and n != 0:
            if m > n:
                m = m % n
            else:
                n = n % m
        return m + n

    ## вспомогательный метод для сокращения дроби
    def __reduce(self):
        nod = self.__nod()
        self.__num = self.__num // nod
        self.__denom = self.__denom // nod

