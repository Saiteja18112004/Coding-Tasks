class Example:
    static_var = 10  # Static variable

obj1 = Example()
obj1.static_var = 20  # This creates an instance variable, not changing the class variable

print(Example.static_var)  # Still 10 (class variable remains unchanged)
print(obj1.static_var)     # 20 (instance variable)
