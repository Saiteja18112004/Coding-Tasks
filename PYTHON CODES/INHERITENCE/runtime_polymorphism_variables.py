class A:
    def __init__(self):
        self.var = "A's variable"

class B(A):
    def __init__(self):
        super().__init__()
        self.var = "B's variable"

class C(B):
    def __init__(self):
        super().__init__()
        self.var = "C's variable"

# Main
if __name__ == "__main__":
    objA = A()
    objB = B()
    objC = C()

    print(objA.var)  # A's variable
    print(objB.var)  # B's variable
    print(objC.var)  # C's variable

    # Using superclass reference
    ref = B()
    print(ref.var)  # B's variable

    ref = C()
    print(ref.var)  # C's variable
