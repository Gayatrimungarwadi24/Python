class Parent:
    def func1(self):
        print("This function belongs to Parent class")

class Child(Parent):
    def func2(self):
        print("This function belongs to Child class")

obj=Child()
obj.func1()
obj.func2()