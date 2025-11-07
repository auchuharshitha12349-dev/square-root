#Program 21
#WAP to input number and print its square if it is odd, otherwise print square root
#source code
x=float(input('enter the number:'))
import math
a=math.pow(x,2)
b=math.sqrt(x)
if x%2!=0:
    print('The value of square is:',a)
else:
    print('The value of square root is:',b)
          
    
