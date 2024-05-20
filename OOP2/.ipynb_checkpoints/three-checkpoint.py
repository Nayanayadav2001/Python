class Employee:
    org_name='tcs'

    def set_ename(self,name):
        self.ename=name
    def set_esal(self,sal):
        self.set_esal=sal

e1=Employee()
e1.set_ename('Nayana')
e1.set_esal(45000)

e2=Employee()
e2.set_ename("Shru")
e2.set_esal(55000)

e3=Employee()
e3.set_ename("siri")
e3.set_esal(65000)

print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)

print(Employee.__dict__)