import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
    result = x/y
    print(result)
except ZeroDivisionError:
    print("Error: Divide by zero")
    sys.exit(1)
except Exception:
    print("Exception occured")
    sys.exit(1)

