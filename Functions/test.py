# def test(num,ran1,ran2):
#     if num in range(ran1,ran2):
#         print('the range is ',num)
#     else:
#         print('the number is outside the range')
# test(20,1,22)

s='Hello Mr Rogers, how are you this fine Tuesday'
def uplow(s):
    d={"upper":0,"lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
            print('original string:',s)
            print('no of upper case character',d["upper"])
            print('no of upper case character',d["lower"])

print(uplow(s))



