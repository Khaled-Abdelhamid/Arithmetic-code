# the file where i test my ideas before embedding them in the code
from fractions import *
print(Fraction(1,5)>Fraction(1,4))

a=[1,2,3,4,5]
print(a[-1])
a.extend([0]*5)
print(a)
a.extend([7])
print(a)

from helpers import *
dic={1: 1, 2: 1, 3: 1, '!': 1}
for i in dic:
    print (i)
    print(Cumfreq(i, dic))
    
