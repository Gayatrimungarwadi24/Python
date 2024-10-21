class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername=grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername=fathername
        Grandfather.__init__(self, grandfathername)

class Daughter(Father):
    def __init__(self, dname, fathername, grandfathername):
        self.dname=dname
        Father.__init__(self, fathername, grandfathername)
        
    def print_name(self):
        print("Grandfather name: ", self.grandfathername)
        print("Father name: ", self.fathername)
        print("Daughter name: ", self.dname)

s1=Daughter("Gayatri", "Pramod", "Ashok")
print(s1.dname)
s1.print_name()