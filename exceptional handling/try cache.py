# try:
#    print(2+'5')
# except:
#     print('there was a tpye errot')
# finally:
#     print('finally this was printed')
#

# def askint():
#     try:
#         val=int(input('enter any integer'))
#         cv=val+4
#         return cv
#     except:
#         print('looks like you did not enter integer')
#         val=int(input('Please enter an integer'))
#         cv=val+4
#         return cv
#     finally:
#         print('finally block executed')
# print(askint())

# def askint():
#     while True:
#         try:
#             value=int(input('please enter an integer'))
#         except:
#             print('soory you did not enter interger')
#             continue
#         else:
#             print('correct that is integer')
#             break
#         finally:
#             print('finally block executed')
# print(askint())

#
# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except:
#     print('an error occured')
# finally:
#     print('all done')

x=0
y=5
try:
    z=y/x
    print('correct',z)
except :
    print('can,t divide by zero')
finally:
    print('all done')


def ask():
    while True:
        try:
            n=int(input('input an integer'))
            x= n**2
            print(x)
        except:
            print('soory you enter incorrect')
            continue
        finally:
            break
    print('thanks')
ask()



