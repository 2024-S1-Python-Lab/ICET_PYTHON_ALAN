class Student:
    def get(self):
        self.rlno=int(input("enter the roll number."))
        self.name=input("enter name.")
        self.totalmark=float(input("enter totalmark."))
    def disp(self):
    
        print(f"roll number.{self.rlno}")
        print(f"name.{self.name}")
        print(f"totalMark:{self.totalmark}")
stud1=Student()
stud1.get()
stud1.disp()
