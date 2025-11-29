import sys

def main():
    script_name = sys.argv[0]

    try:
        # If at least 2 arguments are passed, use them
        if len(sys.argv) >= 3:
            no1 = int(sys.argv[1])
            no2 = int(sys.argv[2])
        else:
            # Defaults if no arguments are given
            no1 = any variables
            no2 = any vaiables
    except ValueError:
        print("❌ Please enter valid integers as arguments.")
        return

    # Perform calculations
    sum_result = no1 + no2
    product = no1 * no2
    difference = no1 - no2

    # Print results
    print(f"Running script: {script_name}")
    print(f"Input values: {no1}, {no2}")
    print(f"Sum = {sum_result}")
    print(f"Product = {product}")
    print(f"Difference = {difference}")

if __name__ == "__main__":
    main()
