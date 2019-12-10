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
dic={1: 7, 2: 5, '!': 1, 7: 2}
for i in dic:
    print (i)
    freqSym=dic[i]
    print('freqSym : ',freqSym)
    S_high=Cumfreq(i,dic)   # get the higher limit of this symbol
    S_low=S_high-freqSym         # get the lower limit of this symbo
    print('S_high : ',S_high)
    print('S_low : ',S_low)
    
