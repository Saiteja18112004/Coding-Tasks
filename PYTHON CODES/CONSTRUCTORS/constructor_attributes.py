class Person:
    def __init__(self, name, age):
        self.name = name  # ✅ Instance attribute
        self.age = age    # ✅ Instance attribute
        print(f"Person Created: {self.name}, {self.age} years old")

if __name__ == "__main__":
    obj = Person("Sai", 20)
    print(f"Name: {obj.name}, Age: {obj.age}")  # ✅ Accessing attributes
