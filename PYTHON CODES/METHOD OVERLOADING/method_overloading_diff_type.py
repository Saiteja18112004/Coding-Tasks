class Example:
    def show(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            print(f"Method with 1 int parameter: {args[0]}")
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], float):
            print(f"Method with 2 parameters (str, float): {args[0]}, {args[1]}")
        else:
            print("Invalid input")

obj = Example()
obj.show(10)             # ✅ Calls int parameter method
obj.show("Hello", 3.14)  # ✅ Calls (str, float) method
