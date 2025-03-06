from child_class import ChildClass

if __name__ == "__main__":
    obj = ChildClass()
    obj.non_abstract_method()  # ✅ Calling the non-abstract method (from AbstractClass)
