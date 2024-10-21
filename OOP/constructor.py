class demo:
    def __init__(self, str):
        self.str=str

    def display(self):
        print(self.str)

obj=demo("Welcome")
obj1=demo("Hello World")
obj.display()
obj1.display()