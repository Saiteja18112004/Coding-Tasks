class Example:
    static_var = 10  # Static variable

Example.static_var = 30  # Changing static variable at the class level

print(Example.static_var)  # 30
