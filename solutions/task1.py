
import string
import math
def fourDigit():
    num = input()
    if (len(num) == 4):
        some = int(int(num[1]) + int(num[2]))
        print(str(some))
    else:
       print("Error!")
       
fourDigit()