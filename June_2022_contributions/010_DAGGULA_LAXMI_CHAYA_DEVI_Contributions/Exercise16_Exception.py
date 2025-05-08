# Exception handling

from sys import argv

try:
    product = float(argv[1]) * float(argv[2])
    print("product is ", product)
except:
    print("Error: provide two numbers")
