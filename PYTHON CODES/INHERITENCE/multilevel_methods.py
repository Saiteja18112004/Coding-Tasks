class A:
    def method1(self):
        print("Method1 of Class A")

    def method2(self):
        print("Method2 of Class A")

    def override_method(self):
        print("Overridden method in Class A")

class B(A):
    def method3(self):
        print("Method3 of Class B")

    def method4(self):
        print("Method4 of Class B")

    def override_method(self):
        print("Overridden method in Class B")

class C(B):
    def method5(self):
        print("Method5 of Class C")

    def method6(self):
        print("Method6 of Class C")

    def override_method(self):
        print("Overridden method in Class C")

# Main
if __name__ == "__main__":
    objA = A()
    objB = B()
    objC = C()

    objA.method1()
    objA.method2()
    objA.override_method()

    objB.method1()
    objB.method2()
    objB.method3()
    objB.method4()
    objB.override_method()

    objC.method1()
    objC.method2()
    objC.method3()
    objC.method4()
    objC.method5()
    objC.method6()
    objC.override_method()
