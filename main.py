from helpers import *
import numpy as np

# in this code we will use integer based arithmatic code insted of the infinte presciosn version 
stream = [1,2,3,4,5,7,85,4,5,7,-5,516,8,1,68,1,313,-5,18,9,7,351,32,15,6,84,13,20,56,85,4,55,6,7,85,4,-5,516,8,1,68,1,313,-5,18,9,7,351,32,15,6,5,5,7,4,5,6,7,86,7,8,8,7,6,85,7,4,5,6,7]
stream=stream*20

precision=32
stream_size=len(stream)+1 # add the end of  file symbol

code,dic =Arithmatic_encode(stream,precision)

print (code)
print (len(code))

message=Arithmatic_decode (code,dic,precision)

stream.pop()

print(stream)     
print (message)
print(stream == message)
        