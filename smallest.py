a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a<b and a<c:
    print(a," is smaller than %d and %d"%(b,c))
elif b<a and b<c:
    print(b," is smaller than %d and %d"%(a,c))
else:
    print(c," is smaller than %d and %d"%(a,c))