class Parent:
    def __init__(self):
        print("Parent Default Constructor Called")

    def __init__(self, a):
        print(f"Parent One-Argument Constructor: a = {a}")

class Child(Parent):
    def __init__(self):
        super().__init__(10)  # ✅ Calling superclass constructor
        print("Child Constructor Called")

if __name__ == "__main__":
    obj = Child()  # ✅ Calls Parent and Child constructor
