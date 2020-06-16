import numpy as np
vec=np.random.uniform(1,20,size=(20))     #getting random values from 1-20 of 1*15 size array
print("Array with random floats are:",vec)
re=vec.reshape((4,5))                     #reshaping from 1*15 to 3*5 array
print("reshaped array is:",re)
x=np.amax(re,axis=1)                      #for getting list of highest value element in array
print("Maximum values in each row are:",x)
#y=np.argmax(re,axis=1)                   #for getting index value of highest value element
#print(y)
print ("Replaced with zeroes in the array",np.where(re==x.reshape(-1,1),0,re)) #using np.where extracting maximum value and reshaping the array
                                                                               # and replacing that value with 0














"""
z=0
for t in y:
    re[z][t]=0
    print(re[z][t])
    z+=1

print(re)
"""

#print(x)