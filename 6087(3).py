##Write a Python program to get the Fibonacci series between 0 to 10
n = int(input("Enter number of terms: "))
n1, n2 = 0, 1
i = 0

if n <= 0:
  print("Please enter a positive integer")
elif n == 1:
  print("Fibonacci sequence upto",n,":")
  print(n1)
else:
  print("Fibonacci sequence:")
  for i in range(n):
      print(n1)
      sum = n1 + n2
      n1 = n2
      n2 = sum