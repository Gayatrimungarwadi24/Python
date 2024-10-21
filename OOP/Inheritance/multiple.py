class Mother:
    mothername=""
    def mothername(self):
        self.mothername=mothername
     
class Father:
    fathername=""
    def fathername(self):
        self.fathername=fathername


class Son(Mother, Father):
    def display(self):
        print("Father: ",self.fathername)
        print("Mother: ",self.mothername)
 
s1=Son()
s1.fathername="Ram"
s1.mothername="Sita"
s1.display()