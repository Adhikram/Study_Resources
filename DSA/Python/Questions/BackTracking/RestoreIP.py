"""
# Question: Restore IP Addresses
# Link: https://leetcode.com/problems/restore-ip-addresses/

# Time Complexity: O(1)
# Space Complexity: O(1)

# Algorithm:
# 1. Use backtracking to generate valid IP addresses
# 2. Validate IP segments
# 3. Build complete IP addresses
# 4. Return all valid combinations

# Key Components:
# - restore_ip_addresses(): Main implementation
# - backtrack(): Recursive helper
# - is_valid_segment(): Segment validation
"""


class RestoreIP:
    def restore_ip_addresses(self, s: str) -> list[str]:
        result = []
        self.backtrack(s, 0, 0, "", result)
        return result

    def backtrack(
        self, s: str, start: int, segment_count: int, current_ip: str, result: list[str]
    ) -> None:
        if segment_count == 4:
            if start == len(s):
                result.append(current_ip[:-1])  # Remove trailing dot
            return

        # Try segments of length 1, 2, and 3
        for length in range(1, 4):
            if start + length > len(s):
                break

            segment = s[start : start + length]
            if self.is_valid_segment(segment):
                self.backtrack(
                    s,
                    start + length,
                    segment_count + 1,
                    current_ip + segment + ".",
                    result,
                )

    def is_valid_segment(self, segment: str) -> bool:
        # Check for leading zeros
        if len(segment) > 1 and segment[0] == "0":
            return False

        # Check value range
        value = int(segment)
        return 0 <= value <= 255


def main():
    solution = RestoreIP()
    s = "25525511135"
    print(
        solution.restore_ip_addresses(s)
    )  # Expected: ["255.255.11.135", "255.255.111.35"]


if __name__ == "__main__":
    main()
