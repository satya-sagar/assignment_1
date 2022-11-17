##Write a program to find the sum of first n numbers using while loop
num=0
a=int(input("Enter the number ="))
while a>0:
    num+=a
    a-=1
print("The sum is",num)