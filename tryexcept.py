# Custom Exceptions


# try:
#     data = int("abc")
# except ValueError as e:
#     raise RuntimeError("Failed to parse number") from e

x = .9
try:
    r = 10/x
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by 0")
else:
    print(f"Completed successfully: {r}")

