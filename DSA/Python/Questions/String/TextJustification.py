"""
# Question: Text Justification
# Link: https://leetcode.com/problems/text-justification/

# Justify text with specific width constraints

# Time Complexity: O(n)
# Space Complexity: O(n)

# Algorithm:
# 1. Process words to fit max width
# 2. Distribute spaces evenly
# 3. Handle last line differently
# 4. Return justified text lines

# Key Components:
# - full_justify(): Main implementation
# - Space distribution logic
# - Last line special handling
"""


class TextJustification:
    def full_justify(self, words: list[str], max_width: int) -> list[str]:
        result = []
        cur_words = []
        cur_len = 0

        for word in words:
            # Check if word fits in current line
            if cur_len + len(word) + len(cur_words) > max_width:
                # Calculate spaces
                total_spaces = max_width - cur_len
                gaps = len(cur_words) - 1

                if gaps == 0:
                    # Single word case
                    result.append(cur_words[0] + " " * total_spaces)
                else:
                    # Distribute spaces evenly
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps

                    line = []
                    for i in range(len(cur_words)):
                        line.append(cur_words[i])
                        if i < gaps:
                            spaces = space_per_gap + (1 if i < extra_spaces else 0)
                            line.append(" " * spaces)

                    result.append("".join(line))

                cur_words = []
                cur_len = 0

            cur_words.append(word)
            cur_len += len(word)

        # Handle last line
        last_line = " ".join(cur_words)
        padding = max_width - len(last_line)
        result.append(last_line + " " * padding)

        return result


def main():
    solution = TextJustification()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 16
    result = solution.full_justify(words, max_width)
    for line in result:
        print(f"'{line}'")


if __name__ == "__main__":
    main()
