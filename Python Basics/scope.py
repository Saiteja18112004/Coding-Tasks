a = "Global Variable"

def fun():
    a = "Local Variable"
    print("Inside function:", a)

fun()
print("Outside function:", a)