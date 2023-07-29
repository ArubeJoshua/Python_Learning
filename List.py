# Sequence data type List
list1 = ["kato", "Joshua", "Joel", "Cosmas", "Mary", "Vanessa"]  # list of strings
list2 = [3, 6, 7, 2, 6]  # list of numbers
list3 = ["a", "j", "m", "l"]  # list of characters

print(type(list1))
print(type(list2))
print(list3)

"""
Lists are changeable
lists allow value repeatition
lists are orederd
"""
list1.append("Jane")
print(list1)

print(len(list1))

# accessing
print(list2[0])  # first item
print(list3[-1])  # last item
print(list1[1:4])
print(list1[:3])
print("John" in list3)

for x in list2:
    print(x)

# changing items
list2[1] = 100
list2[2:4] = [50]
list2.insert(2, 10)
print(list2)

tuple1 = ("Fruit", "Soda")
list1.extend(tuple1)

print(list1)
