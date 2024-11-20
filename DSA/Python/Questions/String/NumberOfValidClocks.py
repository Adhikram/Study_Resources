"""
# Question: Number of Valid Clock Times
# Link: https://leetcode.com/problems/number-of-valid-clock-times/

# Time Complexity: O(1)
# Space Complexity: O(1)

# Algorithm:
# 1. Handle special case "??:??"
# 2. Process hour digits
# 3. Process minute digits
# 4. Calculate total possibilities

# Key Components:
# - count_time(): Main implementation
# - Hour validation
# - Minute validation
"""


class NumberOfValidClocks:
    def count_time(self, time: str) -> int:
        if time == "??:??":
            return 24 * 60

        result = 1

        # Handle hour digits
        if time[0] == "?" and time[1] == "?":
            result *= 24
        elif time[0] == "?":
            result *= 3 if int(time[1]) >= 4 else 2
        elif time[1] == "?":
            result *= 4 if int(time[0]) >= 2 else 10

        # Handle minute digits
        if time[4] == "?":
            result *= 10
        if time[3] == "?":
            result *= 6

        return result


def main():
    solution = NumberOfValidClocks()
    print(solution.count_time("?5:00"))  # Expected: 2
    print(solution.count_time("0?:0?"))  # Expected: 100
    print(solution.count_time("??:??"))  # Expected: 1440


if __name__ == "__main__":
    main()
