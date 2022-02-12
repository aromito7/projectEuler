def gcd(x,y):
    x=abs(x)
    y=abs(y)
    while y>0:
        t=x%y
        x=y
        y=t
    return x

def row_gcd(r):
    x=gcd(r[0],r[1])
    for i in range(2,len(r)):
        x=gcd(x,r[i])
    return x

def lcm(n):
    o=1
    for x in n:
        o//=gcd(o,x)
        o*=x
    return o

class fraction:
    def __init__(self,n,d):
        self.n=n
        self.d=d
        if n==0 and d==0:self.d=1
    def __add__(self,of):
        on=self.n*of.d+of.n*self.d
        od=self.d*of.d
        return fraction(on,od).reduce()
    def __sub__(self,of):
        on=self.n*of.d-of.n*self.d
        od=self.d*of.d
        return fraction(on,od).reduce()
    def __mul__(self,of):
        on=self.n*of.n
        od=self.d*of.d
        return fraction(on,od).reduce()
    def __truediv__(self,of):
        on=self.n*of.d
        od=self.d*of.n
        return fraction(on,od).reduce()
    def reduce(self):
        div = gcd(self.n,self.d)
        if self.d<0:div*=-1
        self.n//=div
        self.d//=div
        return self
    def __str__(self):
        if self.d == 1: return str(self.n)
        else: return str(self.n) + "/" + str(self.d)