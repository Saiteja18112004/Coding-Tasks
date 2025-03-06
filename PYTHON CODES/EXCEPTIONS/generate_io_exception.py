try:
    f = open("/root/protected.txt", "w")  # OSError (Permission denied)
except OSError as e:
    print(f"I/O Error: {e}")
