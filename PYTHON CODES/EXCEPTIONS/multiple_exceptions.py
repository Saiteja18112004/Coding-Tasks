try:
    x = int("abc")  #  ValueError
    y = 10 / 0      #  ZeroDivisionError
except ValueError:
    print("ValueError occurred!")
except ZeroDivisionError:
    print("ZeroDivisionError occurred!")
