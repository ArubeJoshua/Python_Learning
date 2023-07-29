# Datatype dictionary
# dictionaries have keys and their respective values
accessories = dict(
    {
        "phone": "Samsung",
        "speaker": "Djack",
        "TV_set": "Hisence",
        "guitar": "Yamaha",
        "quantity": 50,
        "jewels": ["handband", "wrist watch", "necklace"],
    }
)

print(accessories)  # prints dictionary

# getting the length
print(len(accessories))

print(type(accessories))  # prints data type

# Accessing items in the dictionary
print(accessories.items())  # prints the keys and values in a list of tuples
print(accessories["phone"])
print(accessories["quantity"])

# using get method
y = accessories.get("jewels")
print(y)

# getting keys
x = accessories.keys()
print(x)


# Exercise one: printing all values in the dictionary using values() method
for a in accessories.values():
    print(a)


# Exercise two: check if a key exists
if "phone" in accessories.keys():
    print("true")
else:
    print("false")


# Excercise 3: change, update
# making changes
accessories["quantity"] = 100
accessories.update({"phone": "iphone"})

# Adding another key and avlue
# accessories['beats'] = "JBL"
print(accessories)
# can also use the update function
accessories.update({"microphone": "ibanez"})


# Exercise 4: add, remove items
# Removing items
accessories.pop("quantity")
accessories.popitem()  # removes last item
accessories.clear()  # removes items from the dictionary


# Exercise 5:loop through, nest dicts
# using a loop to access items in dictionaries
for key, value in accessories.items():
    print(key, value)

# using a loop to access keys
for n in accessories.keys():
    print(n)


# Nested dictionaries

family_tree = {
    "fam1": {"name": "Joshua", "num": 10},
    "fam2": {"name": "Joan", "num": 5},
}

print(family_tree["fam1"]["name"])


# Number DATA TYPES
# int
x_int = 1
y_int = -65

print(type(x_int))
print(type(y_int))

# float
x_f = 1.66
y_f = -65.09

print(type(x_f))
print(type(y_f))

# complex
x_c = 1j
y_c = -65j

print(type(x_c))
print(type(y_c))

# type conersion
a_int = 500

a_f = float(a_int)  # conerts 500 int to float
print(type(a_f), a_f)

a_c = complex(a_f)  # converts a_f into a complex
print(type(a_c), a_c)


# casting
# define the data type, complex cannot be defined
age = int(49)
name = str("hello")


# Strings
# Exercise one determining the length using len()
my_name = "Arube Joshua"
str_length = len(my_name)
print(str_length, my_name)

# Exercise two using a loop
for i in my_name:
    if i == " ":
        break
    print(i)

# Exercise three Using slicing
# return a given range of characters
print(my_name[2:7])
print(my_name[:5])

# Conacatenation(addition of strings)
f = "Hello"
l = "There"

print(f + l + "How are you doing")

# format strings
stmt = "My name is Jo am {} years"
age = 21
print(stmt.format(age))


# Booleans

# Exercise
if 4 < 6:
    print("True")
else:
    print("False")
