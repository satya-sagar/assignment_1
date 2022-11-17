##Write a program that prints the numbers from 1 to 100. But for multiples of three print
##“godly” instead of the number and for the multiples of five print “badly”. For numbers
##which are multiples of both three and five print “GodlyBadly”.

for i in range(101):
    if i%3==0 and i%5==0:
        print(i,"GodlyBadly")
    elif i%5==0:
        print(i,"badly")
    elif i%3==0:
        print(i,"godly")
    else:
        print(i)