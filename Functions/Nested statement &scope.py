# global variables your are using
# x='ahmad'
# def loc():
#     return x
# print(loc())


# local and global variables
# x= 50
# def name():
#     x=20
#     return x
#
# print(x)
# print(name())


# enclosing functions'
# x='this is a global variable function'
# def c():
#     x='XYZ'
#
#     def cl():
#     print('hello '+x)
#     cl()
# c()

# local variable

# x=  20
# def loc(x):
#     print('number is ', x)
#     x=40
#     print('now the ', x)
# loc(x)
# print('now the x will be',x)



# global variable
x=100
def func():
    global x
    print('the function is now using the global x')
    print('global variable is',x)
    x=2
    print('now the var is',x)
print('you can check the variable',x)
func()




