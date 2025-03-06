class A:
    def __init__(self):
        self._protected_var = "Protected Variable"

    def _protected_method(self):
        print("This is a protected method")

class B(A):
    def access_protected(self):
        print(self._protected_var)  # ✅ Accessible within subclass
        self._protected_method()    # ✅ Accessible within subclass

if __name__ == "__main__":
    objA = A()
    print(objA._protected_var)  # ✅ Accessible within the same module
    objA._protected_method()    # ✅ Accessible within the same module

    objB = B()
    objB.access_protected()     # ✅ Accessing from subclass
