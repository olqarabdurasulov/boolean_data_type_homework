import math
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return bool(int(math.sqrt(a)) == a)
print(main(9))
print(math.sqrt(9))