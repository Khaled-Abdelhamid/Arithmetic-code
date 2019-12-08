from helpers import *

# in this code we will use integer based arithmatic code insted of the infinte presciosn version 

stream = [1,2,3]
precision=8
stream_size=len(stream)

code =Arithmatic_encode(stream,precision)
print (code)
code_size=len(code)

# those numbers will be used later in the scaling and emitting step of the binary bits
full =2**precision
half=full/2
quarter=half/2

L=0 # the lower limit of the range
H=full # the upper limit of the range

val=0 # a variable to trace how deep i entered at the corner case of which the low and high limits are lying in the middle of the range
indx=1

dic=getfreqs(stream) #output the the dictionary that contains the probabilities of  all ymbols
message=[]

while indx < precision and indx < code_size:# first get the exact amount of values that can be held in the precsion available , the rest will be used during the code
    if code[indx-1]==1:
        val=val+2**(precision-indx)
    indx+=1
flag=1
while flag:
    
    for symbol in dic:  
        
        freqSym=dic[symbol]    # get the frequency of the symbol
        
        S_high=Cumfreq(symbol,dic)   # get the higher limit of this symbol
        S_low=S_high-freqSym             # get the lower limit of this symbol
        Range=H-L                   # get the range of the code  
        
        H0 = L + round( Range * S_high/stream_size )
        L0 = L + round( Range * S_low /stream_size )
        
        if  L0 <=val and val<H0:
            message.extend([symbol])
            L=L0
            H=H0 
            if symbol == '!':
                flag=0
    while H < half or L > half:
        if H < half : # if the range is in the lower half
            L*=2
            H*=2
            val*=2
        elif L > half : # if the range is in the upper half
            L=2*(L-half)
            H=2*(H-half)
            val=2*(val-half)
        if indx<= stream_size and code[indx-1]==1:
            val+=1
            indx+=1
        while L>quarter and H < 3*quarter:
            L=2*(L-quarter)
            H=2*(H-quarter)
            val=2*(val-quarter)
            if indx<= stream_size and code[indx-1]==1:
                val+=1
            indx+=1
                
print (message)