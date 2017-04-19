#
# class employee():
#     raise_amount= 1000
#     num_of_employees=0
#
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+'.'+last+ '@gmail.com'
#         employee.num_of_employees=+1
#
#     def fullname(self):
#         return '{}{}'.format(self.first,self.last)
#
#     def apply_raise(self):
#         return  int(self.pay + self.raise_amount)
#
# print(employee.num_of_employees)
# emp1=employee('bilal','ahmad',5000)
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
# emp1.raise_amount=2000
# print(emp1.apply_raise())
# emp1.raise_amount=2000
# print(emp1.raise_amount)
# print(emp1.__dict__)
# print(employee.__dict__)
# print(employee.num_of_employees)
#
#
#


class employee:
    raise_amount=2000
    no_of_employess=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+ '@gmail.com'
        employee.no_of_employess+=1

    def fullname(self):
        return self.first +'.' +self.last

    def applyraise(self):
        return int(self.pay + self.raise_amount)
print(employee.no_of_employess)
emp1=employee('bilal','ahmad',1000)
emp2=employee('sami','ahmad',5000)

print(employee.__dict__)
print(emp1.fullname())
print(emp1.applyraise())
print(emp2.applyraise())
print(employee.no_of_employess)







