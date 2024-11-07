time=int(input("Enter the time(0-23):"))
if 0>=time<12:
    print("Good Morning")
elif 12>=time<17:
    print("Good Afternoon")
elif 17>=time<20:
    print("Good Evening")
elif 20>=time<=23:
    print("Good Night")
else:
    print("Invalid Time")


    