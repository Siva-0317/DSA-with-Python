# power of two problem
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
# Example usage
if __name__ == "__main__":
    try:
        n = int(input("Enter a number to check if it is a power of two: "))
        if is_power_of_two(n):
            print(f"{n} is a power of two.")
        else:
            print(f"{n} is not a power of two.")
    except ValueError:
        print("Please enter a valid integer.")