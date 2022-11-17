##Write a Python program to count the number of even and odd numbers from a series of numbers
a=int(input("Enter the starting number of the series ="))
b=int(input("Enter the ending number of the series ="))
even=0
odd=0

for i in range(a,b+1):
    if i%2==0:
        even+=1
    else:
        odd+=1

print("Total number of evens are",even,"and odds are",odd)