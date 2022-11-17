##Write a program to calculate factorial of a number using for loop.
a=int(input("Enter the factorial number ="))
fct=1
for i in range(1,a+1):
    fct*=i
print("The factorial of",a,"is",fct)