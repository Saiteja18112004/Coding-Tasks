from abstract_class import AbstractClass

class ChildClass(AbstractClass):
    def __init__(self):
        super().__init__()
        print("Child class constructor")

    def abstract_method(self):
        print("Implementation of abstract method in ChildClass")

if __name__ == "__main__":
    obj = ChildClass()
    obj.non_abstract_method()  # ✅ Accessing non-abstract method from abstract class
