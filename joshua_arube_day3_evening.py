# Exercise 1 Lists
# 1
students = ["Joshua", "Mike", "Sandra", "John", "Grace"]
print(students[1])

# 2
students[0] = "James"
print(students)

# 3
students.append("James")
print(students)

# 4
students.insert(2, "Bathel")
print(students)

# 5
students.pop(3)
print(students)

# 6
print(students[-1])

# 7
fruits = ["mangoes", "oranges", "pineapples", "apples", "grapes", "lemon", "bananas"]
print(fruits[2:5])

# 8
countries = ["Uganda", "Kenya", "Tanzania", "China", "USA"]
copy_countries = countries.copy()
print(copy_countries)

# 9
for country in countries:
    print(country)

# 10
animals = ["Lion", "Cat", "Elephant", "Zebra"]
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)

# 11
with_a = []
for animal in animals:
    if "a" in animal:
        with_a.append(animal)

print(with_a)

# 12
first_name = [
    "Joshua",
]
last_name = [
    "Arube",
]

full_name = first_name + last_name
print(full_name)


# Exercise 2 Tuples
# 1
x = ("samsung", "iphone", "tecno", "redmi")
print(x[0])

# 2
print(x[-2])

# 3
list_x = list(x)
list_x[1] = "itel"
x = tuple(list_x)
print(x)

# 4
x = x + ("Huawei",)
print(x)

# 5
for phone in x:
    print(phone)

# 6
update_x = list(x)
update_x.pop(0)
x = tuple(update_x)
print(x)

# 7
uganda_cities = tuple(["Kampala", "Entebbe", "Gulu", "Mbarara"])
print(uganda_cities)

# 8
(phone1, phone2, phone3, phone4) = x
print(phone1, phone2, phone3, phone4)

# 9
print(x[1:4])

# 10
first = ("Joshua",)
second = ("Arube",)
full = first + second
print(full)

# 11
colors = ("black", "yellow", "blue")
mul_colors = colors * 3
print(mul_colors)

# 12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
times = thistuple.count(8)
print(times)


# Exercise 3 Sets
# 1
fav_beverages = set({"yoghurt", "juice", "coffee"})
print(fav_beverages)

# 2
fav_beverages.update({"water", "milk"})
print(fav_beverages)

# 3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave present")
else:
    print("Microwave is not present")

# 4
mySet.remove("kettle")
print(mySet)

# 5
for y in mySet:
    print(y)

# 6
set_4 = {"one", "two", "three", "four"}
list_2 = ["five", "six"]
set_4.update(list_2)
print(set_4)

# 7
age = {
    21,
}
f_name = {
    "Joshua",
}

comb = age.union(f_name)
print(comb)


# Exercise 4  Strings
# 1
j_age = 21
j_name = "Arube Joshua"
stmt = j_name + " {} "
print(stmt.format(j_age))

# 2
txt = " Hello, Uganda!  "
print(txt.strip().replace(" ", ""))

# 3
print(txt.upper())

# 4
updated_txt = txt.replace("U", "V")
print(updated_txt)

# 5
y = "I am proudly Ugandan"
print(y[1:4])

# 6
# x = “All “Data Scientists” are cool!”
x = "All “Data Scientists” are cool!"
print(x)


# Exercise 5  Dictionaries
Shoes = {"brand": "Nick", "color": "black", "size": 40}

# 1
print(Shoes["size"])

# 2
Shoes["brand"] = "Adidas"
print(Shoes)

# 3
Shoes["type"] = "sneakers"
print(Shoes)

# 4
print(Shoes.keys())

# 5
print(Shoes.values())

# 6
if "size" in Shoes.keys():
    print("true")
else:
    print("false")

# 7
for key, value in Shoes.items():
    print(key, value)

# 8
Shoes.pop("color")
print(Shoes)

# 9
Shoes.clear()
print(Shoes)

# 10
car = {"model": 2017, "type": "merceedes"}
car_copy = car.copy()
print(car_copy)


# 11
family_tree = {
    "fam1": {"name": "Joshua", "num": 10},
    "fam2": {"name": "Joan", "num": 5},
}

print(family_tree["fam1"]["name"])
