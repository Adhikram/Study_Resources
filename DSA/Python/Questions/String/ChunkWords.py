"""
# Question: Chunk Words
# Link: (Custom Problem)

# Problem Statement:
# Given a text string, split it into chunks where each chunk has a maximum size limit.
# The chunks should be split at word boundaries to maintain readability.
# Each chunk should be labeled with its position in the sequence (e.g., "1/3").

# Example:
# Input: text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
# Output: ["Lorem ipsum (1/2)", "dolor sit amet (2/2)"]

# Key Requirements:
# - Maximum chunk size: 160 characters
# - Split at word boundaries only
# - Add position indicators for multiple chunks
"""

from typing import List


class TextChunker:
    def chunk_text(self, text: str, limit: int = 35) -> List[str]:
        """
        Split text into chunks with size constraints
        Time Complexity: O(n) where n is the length of text
        Space Complexity: O(n) for storing chunks
        """
        if not text:
            return []

        chunks = []
        start = 0
        last_space = 0
        n = len(text)

        # Process text character by character
        for i in range(n):
            # Track the last space position
            if text[i] == " ":
                last_space = i

            # Check if current segment exceeds limit
            if i - start >= limit - 6:  # 6 characters reserved for chunk indicator
                if text[i] != " ":
                    # Split at last space
                    chunks.append(text[start:last_space])
                    start = last_space + 1
                else:
                    # Split at current position
                    chunks.append(text[start:i])
                    start = i + 1

        # Add remaining text as final chunk
        if start < n:
            chunks.append(text[start:])

        # Add chunk indicators if multiple chunks exist
        if len(chunks) > 1:
            total = len(chunks)
            chunks = [f"{chunk} ({i+1}/{total})" for i, chunk in enumerate(chunks)]

        return chunks


def main():
    test_cases = [
        {
            "text": "Lorem ipsum dolor sit amet",
            "expected": ["Lorem ipsum dolor sit amet"],
        },
        {
            "text": "Lorem ipsum dolor sit amet " * 3,
            "expected": [
                "Lorem ipsum dolor sit amet (1/3)",
                "Lorem ipsum dolor sit amet (2/3)",
                "Lorem ipsum dolor sit amet  (3/3)",
            ],
        },
        {"text": "", "expected": []},
    ]

    chunker = TextChunker()
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"Input Text: {test['text'][:50]}...")
        result = chunker.chunk_text(test["text"])
        print(f"Result: {result}")
        print(f"Expected: {test['expected']}")
        assert result == test["expected"], f"Test case {i + 1} failed"


if __name__ == "__main__":
    main()
