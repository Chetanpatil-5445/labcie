import sys

script_name = sys.argv[0]

if len(sys.argv) >= 3:   # check if at least two arguments are provided
    no1 = int(sys.argv[1])
    no2 = int(sys.argv[2])
else:
    no1 = 4
    no2 = 9

sum_result = no1 + no2
product = no1 * no2
difference = no1 - no2

print(f"Sum = {sum_result}")
print(f"Product = {product}")
print(f"Difference = {difference}")
