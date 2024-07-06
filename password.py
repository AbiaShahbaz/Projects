"""
----------------------------------
Project: generates a simple but strong password for user
-uses random class
-can be used in real life
----------------------------------
Author: Abia Shahbaz
----------------------------------
"""
# Imports
import random 

#prints welcome message
print("---Welcome to Random Password Generator!---")

#creating password

#random numberS
num1 =random.randrange(20,30)
num2 =random.randrange(40,60,2)
num3 =random.randint(100,250)

#list of random letters and signss to make password unique
myList =["a","e","i","o","u","b","f","x","z"]
myLar =["T","J","N","S","Y","H","M","R"]
mySign =["$","*","%","@","&"]
#choose 1 choice from each
ch1 = random.choice(myList)
ch2 = random.choice(myLar)
ch3 = random.choice(mySign)

#adding to create a unique number
num4 = num1*num2
print("\n\nHere is your random 10 digit password: ",ch2,num4,ch1,num3,ch3, sep="")

  



