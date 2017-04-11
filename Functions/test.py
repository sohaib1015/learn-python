# def test(num,ran1,ran2):
#     if num in range(ran1,ran2):
#         print('the range is ',num)
#     else:
#         print('the number is outside the range')
# test(20,1,22)

# s='Hello Mr Rogers, how are you this fine Tuesday'
# def uplow(s):
#     d={"upper":0,"lower":0}
#     for c in s:
#         if c.isupper():
#             d["upper"]+=1
#         elif c.islower():
#             d["lower"]+=1
#             print('original string:',s)
#             print('no of upper case character',d["upper"])
#             print('no of upper case character',d["lower"])
#
# print(uplow(s))


# s="My Name is XyZ"
# def name(s):
#     d={'uppercase':0,'lowercase':0}
#     for c in s:
#         if c.isupper():
#             d['uppercase']+=1
#         elif c.islower():
#             d['lowercase']+=1
#             print('original string',s)
#             print('upper case',d['uppercase'])
#             print('lower case',d['lowercase'])
# print(name(s))
# l=[1,2,1,1,3,4,5]
# def unique_list(l):
#     # Also possible to use list(set())
#     x = []
#     for a in l:
#         if a not in x:
#             x.append(a)
#     return x
# print(unique_list(l))

# x=[1,2,3,3,4,4,1,5]
# def unique(x):
#     a=[]
#     for c in x:
#         if c not in a:
#             a.append(c)
#     return a
# print(unique(x))

# x=[3,1,2,2,3,4,2]
# def uniquelist(x):
#     xz=[]
#     for c in x:
#         if c not in xz:
#             xz.append(c)
#     return xz
# x.sort()
# print(uniquelist(x))

# import math
# def is_prime(num):
#     '''
#     Better method of checking for primes.
#     '''
#     # if num % 2 == 0 and num > 2:
#     #     return False
#     for i in range(3, int(math.sqrt(num)) + 1, 2):
#         if num % i == 0:
#             return True
#         else:
#             return False
# print(is_prime(45))
# s=[1,3,5,7]
# def num(s):
#     total=1
#     for a in s:
#         total*=a
#     return total
# print(num(s))

g='bilal'
def backward(g):
    g[::-1]
    return g
print(backward(g))

# def palindrome(q):
#
#     return g
# print(palindrome(g))



















