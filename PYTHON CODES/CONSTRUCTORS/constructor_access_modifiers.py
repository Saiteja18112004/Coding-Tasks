class AccessModifiers:
    def __init__(self):  # Public Constructor
        print("Public Constructor Called")

    def _protected_constructor(self):  # Protected Constructor
        print("Protected Constructor Called")

    def __private_constructor(self):  # Private Constructor
        print("Private Constructor Called")

if __name__ == "__main__":
    obj = AccessModifiers()  # ✅ Public constructor is accessible
    obj._protected_constructor()  # ✅ Accessible (convention: _protected)
    
    # obj.__private_constructor()  # ❌ This will raise an error (private)
