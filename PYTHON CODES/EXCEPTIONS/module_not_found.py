try:
    import nonexistent_module  # ModuleNotFoundError
except ModuleNotFoundError:
    print("Module Not Found!")
