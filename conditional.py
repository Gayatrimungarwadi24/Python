def sum_of_two_no():
    num1=1.5
    num2=6.3
    sum=float(num1)+float(num2)
    print("The sum is ",sum)
sum_of_two_no()   

#Selection statements
#if statement
num=int(input("Enter the number: "))
if num%2==0:
    print("Number is an even number")
else:
    print("Number is odd number")

#if-else statements
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote!!")
else:
    print("You are not eligible to vote!!")

#elif statements
number=int(input("Enter the number: "))
if number==10:
    print("The given number is equal to 10")
elif number==50:
    print("The given number is equal to 50")
elif number==100:
    print("The given number is equal to 100")
else:
    print("The given number is not equal to 10,50 or 100")

#while loops
i=1
while i<=10:
    print(i,end=' ')
    i+=1
else:
    print("Program ends")

#for loops
print("String Iteration")
s="Geeks"
for i in s:
    print(i)    

tuple=(3,4,6,8,9,2,3,8,9,7)
for value in tuple:
    if value%2!=0:
        print(value)
else:
    print("These are odd numbers present in the tuple")

#range
for n in range(3,6):
    print(n)

def for_loop_example():
    n=int(input("Enter the number: "))
    for i in range(0,n):
        print(i)
for_loop_example()

def length_example():
    name=input("Enter your name: ")
    for i in range(0,len(name)):
        print(i)
length_example()

#break, continue, pass
for string in "Python Loops":
    if string=='L':
        break
    print("Current Letter: ",string)

for string in "Python Loops":
    if string=='o' or string=='p' or string=='t':
        continue
    print("Current Letter: ",string)

def pass_example():
    for i in range(0,10):
        pass
    print("Good Bye!")
pass_example()