"""
# Question: Chunk Words
# Split text into chunks with size constraints

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Process text in chunks of maximum size
# 2. Split at word boundaries
# 3. Add chunk indicators
# 4. Handle edge cases

# Key Components:
# - solve(): Main chunking implementation
# - Word boundary detection
# - Chunk size management
"""


def solve(text: str) -> list[str]:
    if text is None:
        return []

    space = 0
    start = 0
    n = len(text)
    result = []
    limit = 160

    if n <= limit:
        result.append(text)
        return result

    # Process text in chunks
    for i in range(n):
        if text[i] == " ":
            space = i

        buffer = 6
        if i - start >= limit - buffer:
            if i < n - 1 and text[i] != " ":
                # Take up to the last space
                result.append(text[start:space])
                start = space + 1
            else:
                # Take up to current position
                result.append(text[start:i])
                start = i + 1

    # Add chunk indicators
    if len(result) > 1:
        for i in range(len(result)):
            index = f" ({i}/{len(result)})"
            result[i] = result[i] + index

    return result


def main():
    # Test cases
    text1 = "Lorem ipsum dolor sit amet"
    print(solve(text1))

    text2 = None
    print(solve(text2))

    text3 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec orci sem."
    print(solve(text3))


if __name__ == "__main__":
    main()
