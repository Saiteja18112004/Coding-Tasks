from PACKAGES import ClassOne, ClassTwo

if __name__ == "__main__":
    obj1 = ClassOne()  # ✅ Calls constructor of ClassOne
    obj1.method_one()  # ✅ Calls method of ClassOne

    obj2 = ClassTwo()  # ✅ Calls constructor of ClassTwo
    obj2.method_two()  # ✅ Calls method of ClassTwo
