import math
import digsys

#Z zahlen
class Q: #Quotient
    def __init__(self, num, den):
        self.num = int(num)
        self.den = int(den)
    def __str__(self):
        common = math.gcd(self.num, self.den)
        return "%s/%s" % (self.num//common, self.den//common)
    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        common = math.gcd(newnum, newden)
        return Q(newnum//common, newden//common)
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = math.gcd(newnum, newden)
        return Q(newnum // common, newden // common)
    def __eq__(self, other):
        firstn = self.num*other.den
        second = other.num*self.den
        return firstn == second

class Group:
    def __init__(self, a):
        self.a = a
    def __mul__(self, other):
        return self.a+other.a

def main():
    a = Q(input('Set num:'), input('Set den:'))
    print(type(a.den))
    print(a)
    print(Group.__name__)
    g1 = digsys.AndGate("G1")
    print(g1.getOutput())

if __name__== "__main__":
    main()