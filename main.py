from helpers import *
import numpy as np

# in this code we will use integer based arithmetic code insted of the infinite prescision version 

# creating arbitrary stream to test on 
stream = [1,2,3,4,5,7,85,4,5,7,-5,516,8,1,68,1,313,-5,18,9,7,351,32,15,6,84,13,20,56,85,4,55,6,7,85,4,-5,516,8,1,68,1,313,-5,18,9,7,351,32,15,6,5,5,7,4,5,6,7,86,7,8,8,7,6,85,7,4,5,6,7]
stream=stream*20 # this is just made to increase the size without writing too much :)

 # Unlike the infinite precision case, here we are confined with a finite amount of bits
 # the number of precision bits that from which we will try to handle the code
precision=32

# call the encoder function
code,dic =Arithmetic_encode(stream,precision)

print (code)
print ('number of bits is : ',len(code))

# call the decoder function
message=Arithmetic_decode (code,dic,precision)

stream.pop()# remove the end of file symbol so that we could compare the stream with the decoded messsage

print(stream)     
print (message)
print(stream == message)
        