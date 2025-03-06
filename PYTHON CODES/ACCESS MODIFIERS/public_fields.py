class A:
    def __init__(self):
        self.public_var = "Public Variable"

    def public_method(self):
        print("This is a public method")

if __name__ == "__main__":
    objA = A()
    print(objA.public_var)  # ✅ Accessible anywhere
    objA.public_method()    # ✅ Accessible anywhere
