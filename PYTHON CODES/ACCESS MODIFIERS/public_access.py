from public_fields import A

if __name__ == "__main__":
    objA = A()
    print(objA.public_var)  # ✅ Accessible in a different package
    objA.public_method()    # ✅ Accessible in a different package
