import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    no1 = int(sys.argv[1])
    no2 = int(sys.argv[2])
else:
    script_name = sys.argv[0]
    no1 = 4
    no2 = 5

sum_result = no1 + no2
product = no1 * no2
difference = no1 - no2

print(f"Sum = {sum_result}")
print(f"Product = {product}")
print(f"Difference = {difference}")
