def find_max(numbers):
    """Find maximum number in a list"""
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
    """Find minimum number in a list"""
    if not numbers:
        return None
    return min(numbers)

def calculate_average(numbers):
    """Calculate average of numbers in a list"""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    nums = [10, 5, 8, 12, 3, 7]
    print(f"Numbers: {nums}")
    print(f"Max: {find_max(nums)}")
    print(f"Min: {find_min(nums)}")
    print(f"Average: {calculate_average(nums):.2f}")