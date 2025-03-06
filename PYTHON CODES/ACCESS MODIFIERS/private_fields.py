class A:
    def __init__(self):
        self.__private_var = "Private Variable"

    def __private_method(self):
        print("This is a private method")

    def access_private(self):
        print(self.__private_var)
        self.__private_method()

class B(A):
    def try_access_private(self):
        # print(self.__private_var)  # ❌ This will cause an AttributeError
        # self.__private_method()   # ❌ This will cause an AttributeError
        print("Cannot access private members from subclass")

if __name__ == "__main__":
    objA = A()
    objA.access_private()  # ✅ Accessing private members via public method

    objB = B()
    objB.try_access_private()  # ❌ Cannot directly access private members
