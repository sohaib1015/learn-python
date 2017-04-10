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
l=[1,2,1,1,3,4,5]
def unique_list(l):
    # Also possible to use list(set())
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list(l))

