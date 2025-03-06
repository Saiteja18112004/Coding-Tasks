with open("sample.txt", "r") as file:
    file.seek(15)  # Move to the 15th byte
    print(file.read(10))  # Read 10 characters from there
