"""
# Question: Decode String
# Convert numeric strings to alphabetic representation

# Time Complexity: O(2^n)
# Space Complexity: O(n)

# Algorithm:
# 1. Create alphabet mapping (1-26 to A-Z)
# 2. Recursively decode substrings
# 3. Track valid decodings
# 4. Handle edge cases

# Key Components:
# - create_alphabet_map(): Generate number to letter mapping
# - decode(): Recursive decoder implementation
        "121" -> "ABA", "AU", "LA" -> 3
        "1234" -> "ABCD", "LCD", "AWD" -> 3
        “96” -> “IF” -> 1
        “90” → 0
"""



def decode(s: str) -> int:

    result = 0
    if int(s) in range(1, 27):
        result = 1

    n = len(s)
    for part in range(1, n):
        right_part = s[part:n]
        right_result = decode(right_part)
        result += right_result

    return result


def main():
    print(decode("121"))  # Expected: 3
    print(decode("1234"))  # Expected: 4
    print(decode("96"))  # Expected: 1
    print(decode("90"))  # Expected: 0


if __name__ == "__main__":
    main()
