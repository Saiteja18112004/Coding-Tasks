try:
    f = open("non_existent.txt", "r")  # FileNotFoundError
except FileNotFoundError as e:
    print(f"File Not Found: {e}")
