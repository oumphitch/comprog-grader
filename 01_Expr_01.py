from math import pi,exp
n = int(input())
lower = (2*pi)**0.5*n**(n+0.5)*(exp(-n+(1/(12*n+1))))
higher = (2*pi)**0.5*n**(n+0.5)*(exp(-n+(1/(12*n))))
print(lower)
print(higher)
