class MyClass:
    def __init__(self):
        self.name = "Python"

obj = MyClass()
try:
    print(obj.age)  # ❌ AttributeError
except AttributeError as e:
    print(f"Attribute Error: {e}")
