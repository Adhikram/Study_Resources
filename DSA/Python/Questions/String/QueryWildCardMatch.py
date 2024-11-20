"""
# Question: Query Wildcard Match
# Pattern matching with wildcard characters

# Time Complexity: O(n*m)
# Space Complexity: O(n*m)

# Algorithm:
# 1. Recursive pattern matching
# 2. Handle wildcard characters
# 3. Process text and query strings
# 4. Track matching positions

# Key Components:
# - question_wildcard_match(): Main implementation
# - helper(): Recursive matching function
# - Test case validation
"""


def helper(text: str, query: str, t_index: int, q_index: int) -> bool:
    if q_index == len(query):
        return True

    if t_index == len(text):
        return False

    # Handle 'x?' pattern
    query_char = query[q_index]
    if q_index + 1 < len(query) and query[q_index + 1] == "?":
        # Skip the next char
        if helper(text, query, t_index, q_index + 2):
            return True
        # Take this char
        if text[t_index] == query_char or query_char == ".":
            return helper(text, query, t_index + 1, q_index + 2)
        return helper(text, query, t_index + 1, 0)

    if text[t_index] == query[q_index] or query[q_index] == ".":
        return helper(text, query, t_index + 1, q_index + 1)
    return helper(text, query, t_index + 1, 0)


def question_wildcard_match(text: str, query: str) -> bool:
    if not query:
        return True

    if query.startswith("?") or "??" in query:
        return False

    return helper(text, query, 0, 0)


def print_test_case(text: str, query: str, expected: bool) -> None:
    result = question_wildcard_match(text, query)
    print(f'Input: text = "{text}", query = "{query}"')
    print(f"Expected: {expected}, Actual: {result}")
    assert (
        result == expected
    ), f'Test case failed for input: text = "{text}", query = "{query}"'


def main():
    test_cases = [
        ("hello world", "hel?lo", True),
        ("hello world", "ll?o", True),
        ("hello world", "hell?l?l?o?o?", True),
        ("hello world", "hell?o?o", True),
        ("hello world", "hell?lo", True),
        ("hello world", "world?", True),
        ("hello world", "worldd?", True),
        ("hello world", ".?ell?l?l?o?o?", True),
    ]

    for text, query, expected in test_cases:
        print_test_case(text, query, expected)


if __name__ == "__main__":
    main()
