class Fraction_pkg:
    def __init__(self, a, b):
        self.a= a
        self.b= b
    
    def __str__(self):
        return "{}/{}".format(self.a, self.b)

    def __add__(self, other):
        num= (self.a * other.b) + (self.b * other.a)
        den= (self.b * other.b)
        return "{}/{}".format(self.num, self.den)

