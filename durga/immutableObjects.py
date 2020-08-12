x = 10
print(id(x))
x = 10 + 1
print(id(x))

# o/p:
# 4351483856
# 4351483888

myList = [10,20,30]
print(id(myList))
myList[0] = 7777
print(id(myList))
print(myList)