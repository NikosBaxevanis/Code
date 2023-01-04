import sys

names = ["bill" , "charlie" , "fred" , "george"]

if "george" in names:
    print("found")
    sys.exit(0)

print("not found")
sys.exit(1)