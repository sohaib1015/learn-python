# Python uses file objects to interact with external files on your computer.
# These file objects can be any sort of file you have on your computer
#
# read the file through
# f.read method

# This happens because you can imagine the reading "cursor" is at the end of the file after having read it.
#  So there is nothing left to read. We can reset the "cursor" like this:
# g.seek

g = open('lists.py')
print(g.read)
print(g.seek(0))
print(g.read())






