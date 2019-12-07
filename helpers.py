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
