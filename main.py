from helpers import *

# in this code we will use integer based arithmatic code insted of the infinte presciosn version 


stream = [1,2,3,3,3,3,3]
stream.append('!')

StreamSize=len(stream)

dic=getfreqs(stream) #output the the dictionary that contains the probabilities of  all ymbols
syms_no=len(dic)#gets the numbers of symbols
print (dic)
symbol=0
index=0

precision=32 #the number of persicion bits 
# those numbers will be used later in the scaling and emitting step of the binary bits
full =2**precision
half=full/2
quarter=half/2

L=0 # the lower limit of the range
H=full # the upper limit of the range
trails=0 # a variable to trace how deep i entered at the corner case of which the low and high limits are lying in the middle of the range


code = [] # the list that will include the comressed code 

while symbol != '!':
    
    symbol=stream[index]# aquire the symbol from the stream
    index+=1
    
    psym=dic[symbol]    # get the probability of the symbol
    
    S_high=Cumfreq(symbol,dic)   # get the higher limit of this symbol
    S_low=S_high-psym             # get the lower limit of this symbol
    
    Range=H-L                   # get the range of the code     
    
    # the rounding happens to gurantee that everything is integer
    H = L + round( Range * S_high/StreamSize )
    L = L + round( Range * S_low /StreamSize )



