"""
# Question: Next Closest Time
# Link: https://leetcode.com/problems/next-closest-time/

# Time Complexity: O(1)
# Space Complexity: O(1)

# Algorithm:
# 1. Extract unique digits from time
# 2. Generate next valid time
# 3. Handle digit replacement
# 4. Validate time constraints

# Key Components:
# - next_closest_time(): Main implementation
# - Time validation
# - Digit selection
"""


class NextClosestTime:
    def next_closest_time(self, time: str) -> str:
        # Extract unique digits
        digits = sorted(set(time.replace(":", "")))

        # Process current time
        curr = time.split(":")
        curr_hour = int(curr[0])
        curr_min = int(curr[1])

        # Try all possible combinations
        while True:
            curr_min += 1
            if curr_min == 60:
                curr_min = 0
                curr_hour += 1
                if curr_hour == 24:
                    curr_hour = 0

            # Convert current time to string
            curr_time = f"{curr_hour:02d}:{curr_min:02d}"

            # Check if all digits are valid
            valid = True
            for digit in curr_time:
                if digit != ":" and digit not in digits:
                    valid = False
                    break

            if valid:
                return curr_time


def main():
    solution = NextClosestTime()
    print(solution.next_closest_time("19:34"))  # Expected: "19:39"
    print(solution.next_closest_time("23:59"))  # Expected: "22:22"


if __name__ == "__main__":
    main()
