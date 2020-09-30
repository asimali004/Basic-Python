import numpy as np
import pandas as pd
import random

while(True):
    print("Input the size of one side of square matrix in range 8-20")
    i=int(input())#asking the user to enter the size of the square matrix
    if i>=8 and i<=20:#checking if he entered the size in range
        break#Required value taken exactly

h=np.random.randint(0,9,(i,i))#creating a random square matrix of given size
a=pd.DataFrame(h)#converting the numpy array to dataframe so that it can be altered easily
p=a[0][0]#The liquid that will start from top left corner
r=0#a variable to alter the no of rows
c=0#a variable to alter the no of columns
sum=0#sum of the integers through which the number will flow
while r<=i-1 and c<=i-1:#checking if the liquid have reached an edge
    n=np.random.randint(1,3)#randomly moving the liquid
    if n==1:#moving right side if n is 1 which is randomly generated
        sum=sum+a[c][r]#adding the no to the sum through which the liquid has passed
        a[c][r]=15#replacing the passed no with number 15
        c=c+1
    else:#moving downward if n!=1 which is randomly generated
        sum=sum+a[c][r]
        a[c][r]=15
        r=r+1
a=a.replace(15,"+")#making the path of the liquid visible using "+"

print("The Movement of liquid is shown using + symbol")
print(a)

print("The sum of the integers through which the liquid passed is ",sum)

h=np.random.randint(0,9,(i,i))
b=pd.DataFrame(h)#converting the numpy array to dataframe so that it can be altered easily
p=b[0][0]#The liquid that will start from top left corner
r=0#a variable to alter the no of rows
c=0#a variable to alter the no of columns
sum=0#sum of the integers through which the number will flow
while r<=i-1 and c<=i-1:#checking if the liquid have reached an edge
    n=np.random.randint(1,3)#randomly moving the liquid
    if n==1:#moving right side if n is 1 which is randomly generated
        sum=sum+b[c][r]#adding the no to the sum through which the liquid has passed
        b[c][r]=15#replacing the passed no with number 15
        r=r+1
        flag =True
    else:#moving downward if n!=1 which is randomly generated
        sum=sum+b[c][r]
        b[c][r]=15
        c=c+1
        flag= False
b=b.replace(15,"+")#making the path of the liquid visible using "+"
if flag==False:
    c=c-1
while r<=i-1:
    b[c][r]=15
    r=r+1
b=b.replace(15,"+")

print("The Movement of liquid is shown using + symbol")
print(b)

print("The sum of the integers through which the liquid passed is ",sum)

h=np.random.randint(0,9,(i,i))#creating a random square matrix of given size
d=pd.DataFrame(h)#converting the numpy array to dataframe so that it can be altered easily
c=int(input("Enter the column no from where you want to start liquid flow"))
r=int(input("Enter the row no from where you want to start liquid flow"))
sum=0#sum of the integers through which the number will flow
while r<=i-1 and c<=i-1:#checking if the liquid have reached an edge
    n=np.random.randint(1,3)#randomly moving the liquid
    if n==1:#moving right side if n is 1 which is randomly generated
        sum=sum+d[c][r]#adding the no to the sum through which the liquid has passed
        d[c][r]=15#replacing the passed no with number 15
        c=c+1
        flag=False
    else:#moving downward if n!=1 which is randomly generated
        sum=sum+d[c][r]
        d[c][r]=15
        r=r+1
        flag=True
d=d.replace(15,"+")#making the path of the liquid visible using "+"

if flag==False:
    c=c-1
while r<=i-1:
    d[c][r]=15
    r=r+1
d=d.replace(15,"+")

print("The Movement of liquid is shown using + symbol")
print(d)

print("The sum of the integers through which the liquid passed is ",sum)
