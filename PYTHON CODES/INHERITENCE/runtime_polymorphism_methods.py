class A:
    def override_method(self):
        print("Overridden method in Class A")

class B(A):
    def override_method(self):
        print("Overridden method in Class B")

class C(B):
    def override_method(self):
        print("Overridden method in Class C")

# Main
if __name__ == "__main__":
    refB = A()
    refB.override_method()  # A's method

    refB = B()
    refB.override_method()  # B's method

    refC = A()
    refC.override_method()  # A's method

    refC = C()
    refC.override_method()  # C's method
