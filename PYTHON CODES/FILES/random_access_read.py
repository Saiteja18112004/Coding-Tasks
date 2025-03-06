with open("sample.txt", "r") as file:
    file.seek(5)  # Move cursor to the 5th byte
    content = file.read(10)  # Read next 10 characters
    print(content)
