class Student:
    def get(self,rlno,name,totalmark):
        self.rlno=rlno
        self.name=name
        self.totalmark=totalmark
    def disp(self):
        print(f"roll Number.{self.rlno}")
        print(f"name:{self.name}")
        print(f"totalMark:{self.totalmark}")
stud1=Student()
stud1.get(101,"Alice",85)
stud1.disp()
