import numpy as np

def increment_x_value ():
   nplist= np.array([1,1,1,1,1,1,1,1])
   nplength = len(nplist)
   x = 0

   for i in range (nplength):
      x = x +1

   return (x)

result = increment_x_value()
print (result)


