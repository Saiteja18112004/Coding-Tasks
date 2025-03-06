with open("sample.txt", "rb") as file:
    chunk = file.read(10)  # Reads the first 10 bytes
    print(chunk)
