# class employee():
#     pass
#
# emp_1=employee()
# emp_2=employee()
#
# emp_1.firstname='bilal'
# emp_1.lastname='ahmad'
# emp_1.email='bilalshakeel590@gmail.com'
#
# emp_2.firstname='sami'
# emp_2.lastname='ahmad'
# emp_2.email='samishakeel590@gmail.com'
#
#
# print(emp_1.email)
# print(emp_2.email)
#

# def __init(self)-->is init method (e.g initialize( if you are coming from other language it is called constructor)
# when we create methods in class it recieve first instances(arguments) automatically

class employee():
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'gmail.com'

    def fullname(self):
        return '{} {}'.format(emp_1.first, emp_1.last)
emp_1=employee('bilal','ahmad',5000)
emp_2=employee('sami','ahmad',3000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())





