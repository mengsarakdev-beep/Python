# 1
numbers = [1, 2, 3, 4, 5]
print(numbers)

# 2
numbers.append(6)

# 3
numbers.insert(0, 0)

# 4
numbers.remove(3)

# 5
numbers.pop(2)

# 6
numbers.sort()

# 7
numbers.reverse()

# 8
my_dict = {"name": "John", "age": 30, "job": "Engineer"}

# 9
print(my_dict["name"])

# 10
my_dict["location"] = "USA"

# 11
del my_dict["age"]

# 12
my_tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = my_tuple

# 13
print(my_tuple[1])

# 14
a,b,c,d,e = my_tuple

# 15
my_set = {1, 2, 3}

# 16
my_set.remove(2)

# 17
print(3 in my_set)

# 18
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# 19
print(set1.intersection(set2))

# 20
nested_dict = {"person": {"name": "John", "age": 30}}
print(nested_dict["person"]["name"])