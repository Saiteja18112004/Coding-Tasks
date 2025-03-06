from protected_fields import A

class C(A):
    def access_protected(self):
        print(self._protected_var)  # ✅ Accessible within subclass (even in a different package)
        self._protected_method()    # ✅ Accessible within subclass

if __name__ == "__main__":
    objC = C()
    objC.access_protected()

    objA = A()
    # print(objA._protected_var)  # ❌ Not accessible from a different package unless subclassed
    # objA._protected_method()   # ❌ Not accessible from a different package unless subclassed
