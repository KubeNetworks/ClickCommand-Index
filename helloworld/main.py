import os

print(" Env ".center(60, "="))

keys = sorted(os.environ)
for item in keys:
    print(item, os.environ[item])
