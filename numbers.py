import math

math.floor(2.5)
# floor will move to the lowest nearest value 
math.ceil(2.6)
# ceil will move to the highest nearest value 

math.trunc(-2.6)
# trunc will move towards the zero of number line


# python has number precision upto a great extent
# python also deals with complex numbers

(2+3j)*3

# python also deal with octal numbers
 


# to find the octal hexal and binary number of any numbe we have methods in python 
oct(65)
hex(64)
bin(64)

# this method will give us the all the value

# we can also get random number in python 
import random
random.random()
# we can also specifiy if we need specific random number like if i want number between 1-10
random.randint(1,9)
# we can also choose random from an array 
l1 = ["math","phy","chem","bio"]
random.choice(l1)

# we can also shuffle it 
random.shuffle(l1)

# we can also deals with decimal number 
from decimal import Decimal
Decimal("0.3")+Decimal("0.3")+Decimal("0.3")
# if we dont import decimal it will give us the wrong value


# we can also deal with fraction in python 
from fractions import Fraction
myFra = Fraction(2,7)


# we can also operate with sets in python 

setone = {1,2,3,4,5}
# intersection of two set
setone & {2,4}
# union of two sets 
setone | {2,3}
# if we minus 
setone - {1,2,3,4,5}
#  we will receive 
# set()
# we will not receive empty branthesis {} becuse it is dictionary