class utils:
    def reversed(self, a):
        sign = -1 if a < 0 else 1 # add positive or negative afterward
        return sign * int(str(abs(a))[::-1]) # use list/string indices to reverse

    def formatter(self, a):
        return bin(a), oct(a)
        