import numpy as np
def getfreqs(stream):
    """
    This function Takes a stream as an input. it gets the number of occurnces of each symbol
    in that stream,  store it in a Dictionary containing every symbol in the stream .
    and returns the Arithmetic code of that stream
    
    Arguments:
        stream {list} -- [description]
    Returns:    
        Dict {dictionary} -- [description]
    """

    symbols = set(stream)   #get the unique elements
    L = len(stream)
    Dict = {}          #store each symbol with its corresponding probability
    #calculate the probability of each symbol in the sream 
    for s in symbols:
        freq = stream.count(s)
        Dict[s] = freq
    return Dict

def Cumfreq(symbol, dictionary):
  
  '''This Function Takes as  inputs a symbol and a dictionary containing
  all the symbols that exists in our stream and their frequencies 
  and returns the cumulative freuency starting from the very 
  beginning of the Dictionary untill that Symbol.
  '''
  P = 0.0
  for sym in dictionary:
      P += dictionary[sym]
      if sym == symbol:
        break
  return P

def CumulativeDict(Dict, start = 0):
    
  ''' This Function Takes as an input a dictionary of symbols its probability,
      and return the Cumulative probability for each symbol. we use it in defining a decimal region for each symbol.
      another parameter can be passed to the function, the starting point of the whole symbols, which is by default zero.
  '''
  CumDict = {}
  
  for symbol in Dict:
    CP = start
    for sym in Dict:
      CP += Dict[sym]
      if sym == symbol:
        break
    CumDict[symbol] = CP
  return CumDict


def Arithmatic_encode (stream,precision=32):
    stream.append('!')

    StreamSize=len(stream)

    dic=getfreqs(stream) #output the the dictionary that contains the probabilities of  all ymbols
    syms_no=len(dic)#gets the numbers of symbols
    print (dic)
    symbol=0
    index=0

    # those numbers will be used later in the scaling and emitting step of the binary bits
    full =2**precision
    half=full/2
    quarter=half/2

    L=0 # the lower limit of the range
    H=full # the upper limit of the range
    trails=0 # a variable to trace how deep i entered at the corner case of which the low and high limits are lying in the middle of the range


    code = [] # the list that will include the comressed code 

    # while symbol != '!':
    for index in range(StreamSize):        
        symbol=stream[index]# aquire the symbol from the stream
        # index+=1
        
        freqSym=dic[symbol]    # get the frequency of the symbol
        
        S_high=Cumfreq(symbol,dic)   # get the higher limit of this symbol
        S_low=S_high-freqSym         # get the lower limit of this symbol
        Range=H-L                    # get the range of the code     
        # if (Range<(quarter+2)):
        #     print("precision error ,try to increase the precision")
        #     break
        # the rounding happens to gurantee that everything is integer
        H = L + round( Range * S_high/StreamSize )
        L = L + round( Range * S_low /StreamSize )
        
        #creating the cases for which we will emmit 0 or 1 to our final code word
        while H < half or L > half: # the first two easy cases , if my range fully falls inside one block
            if H < half : # if the full range falls in the lower half 
                code.extend([0])
                code.extend([1]*trails)
                trails=0
                # scale the lower half to be the full range
                L*=2
                H*=2
            elif L > half:# if the full range falls in the upper half 
                code.extend([1])
                code.extend([0]*trails)
                trails=0
                # scale the upper half to be the full range
                L=2*( L - half )
                H=2*( H - half )
                
        while L > quarter and H < 3*quarter: # if the range is split between the the upper half and the lower half
            trails+=1
            L=2*(L-quarter)
            H=2*(H-quarter)      
    trails+=1
    if L<=quarter:
        code.extend([0])
        code.extend([1]*trails)
    else:
        code.extend([1])
        code.extend([0]*trails)
    return code
