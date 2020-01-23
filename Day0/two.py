set_one = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set_one)
set_one.add(10)
print(set_one)
set_one.update([11, 12, 13])
print(set_one)
set_one.discard(90)
print(set_one)
# set_one.remove(90)#gives key error ,if not present
print(set_one)
print(set_one.pop())
print(set_one.pop())
print(set_one.pop())
print(set_one.pop())
print(set_one.clear())
set_one = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_two = {11, 2, 3, 14, 15, 16, 17, 8, 9}
print("Union", set_one | set_two)
print("Intersection", set_one & set_two)
print("Difference", set_one-set_two)
print("Difference,two", set_two-set_one)
print("Symmetric Difference", set_one ^ set_two)
