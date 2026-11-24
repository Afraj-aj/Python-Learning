name = "Alice"
age = 30

# Without formatted string
greeting = "Hello, my name is " + name + " and I am " + str(age)
print(greeting)

# With formatted string
greeting = f"Hello, my name is {name} and I am {age}"
print(greeting)   # Hello, my name is Alice and I am 30

# Expressions inside braces
result = f"The sum of 2 + 3 is {2 + 3}"
print(result)   # The sum of 2 + 3 is 5

# Using uppercase F works the same
message = F"{name} is {age} years old."
print(message)   # Alice is 30 years old.

# Literal braces are doubled
print(f"{{name}}")  # {name}

# Conversions and format specifications
value = 3.14159
print(f"{value:.2f}")   # 3.14
print(f"{value:.{2}f}")  # 3.14 (nested replacement field in format spec)
print(f"{name!r}")      # 'Alice' (repr conversion)
label = "café"
print(f"{label!a}")     # 'caf\xe9' (ASCII-only repr conversion)
print(f"{label!s}")     # café (str conversion)
print(f"{age=}")        # age=30 (debug form)