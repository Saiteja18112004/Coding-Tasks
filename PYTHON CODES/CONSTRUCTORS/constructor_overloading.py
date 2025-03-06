class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default Constructor Called")
        elif b is None:
            print(f"One-Argument Constructor Called: a = {a}")
        else:
            print(f"Two-Argument Constructor Called: a = {a}, b = {b}")

if __name__ == "__main__":
    obj1 = MyClass()         # ✅ Default constructor
    obj2 = MyClass(10)       # ✅ One-argument constructor
    obj3 = MyClass(10, 20)   # ✅ Two-argument constructor
