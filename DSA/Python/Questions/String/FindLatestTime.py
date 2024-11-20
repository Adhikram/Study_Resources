"""
# Question: Find Latest Time
# Find the latest valid time given a pattern with question marks

# Time Complexity: O(1)
# Space Complexity: O(1)

# Algorithm:
# 1. Process each position in time string
# 2. Replace question marks with valid digits
# 3. Handle hour and minute constraints
# 4. Return formatted time string

# Key Components:
# - find_latest_time(): Main implementation
# - Time validation logic
# - String manipulation
"""


class FindLatestTime:
    def find_latest_time(self, s: str) -> str:
        time_chars = list(s)

        # Handle first digit of hour
        if time_chars[0] == "?":
            if time_chars[1] == "?" or int(time_chars[1]) < 2:
                time_chars[0] = "1"
            else:
                time_chars[0] = "0"

        # Handle second digit of hour
        if time_chars[1] == "?":
            if time_chars[0] == "1":
                time_chars[1] = "1"
            else:
                time_chars[1] = "9"

        # Handle first digit of minute
        if time_chars[3] == "?":
            time_chars[3] = "5"

        # Handle second digit of minute
        if time_chars[4] == "?":
            time_chars[4] = "9"

        return "".join(time_chars)


def main():
    solution = FindLatestTime()
    s = "1?:?8"
    print(solution.find_latest_time(s))


if __name__ == "__main__":
    main()
