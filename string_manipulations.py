# 1 - 4
string = "hello"
print(len(string), string + " world", string * 3, string[0])

# 5 - 8
print(string[-1], string[:3], string.upper(), string.lower())

# 9 - 10
print(string.startswith("h"), string.endswith("o"))

# 11 - 12
print(string.find("e"), string.replace("hello", "hi"))

# 13 - 14
words = "Hello world".split()
print(".".join(words))

# 15
print(" hello ".strip())

# 16
print("hello123".isalnum())

# 17
print(string[::-1])

# 18
print(string.count("l"))

# 19
name, age = "John", 30
print(f"My name is {name}, and I am {age} years old.")

# 20
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))