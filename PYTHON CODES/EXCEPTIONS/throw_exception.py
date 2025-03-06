def faulty_method():
    raise ValueError("Custom Exception Raised")

faulty_method()  # ❌ No try-except, will crash
