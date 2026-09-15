class utils:
    def reversed(self, a: int):
        if not isinstance(a, int): # explicit check for int input
            raise TypeError("a must be an integer")
        sign = -1 if a < 0 else 1 # add positive or negative afterward
        return sign * int(str(abs(a))[::-1]) # use list/string indices to reverse

    def formatter(self, a: int):
        if not isinstance(a, int): # explicit check for int input
            raise TypeError("a must be an integer")
        return bin(a), oct(a) # return both formats as a tuple
        