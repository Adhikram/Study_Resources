"""
# Question: Duplicate Message
# The problem is to filter messages that are duplicated within a 10-second window.

# Rules:
# - If a message type appears multiple times within 10 seconds, remove all occurrences
# - Messages are identified by their first character
# - Time is represented as an integer after the first character

# Time Complexity: O(n) where n is the number of messages
# Space Complexity: O(k) where k is the number of unique message types

# Algorithm:
# 1. Iterate through messages chronologically
# 2. For each message:
#    - Extract message type (first character) and timestamp
#    - Check if message type was seen before
#    - If seen within 10 seconds, skip
#    - If seen after 10 seconds or not seen, add to result
# 3. Update last seen timestamp for message type

# Example:
# Input: ["t1", "t5", "f8", "t11", "t12", "t21", "t23", "g32", "t46"]
# Output: ["f8", "t23", "g32", "t46"]
"""

from typing import List


class DuplicateMessage:
    def __init__(self):
        self.last_seen = {}

    def extract_info(self, message: str) -> tuple:
        """Extract message type and timestamp from message string"""
        return message[0], int(message[1:])

    def solve(self, messages: List[str]) -> List[str]:
        result = []
        self.last_seen.clear()

        for message in messages:
            msg_type, timestamp = self.extract_info(message)

            if msg_type in self.last_seen:
                prev_time = self.last_seen[msg_type]
                if timestamp - prev_time > 10:
                    result.append(message)
            else:
                result.append(message)

            self.last_seen[msg_type] = timestamp

        return result


def main():
    duplicate_message = DuplicateMessage()
    messages = ["t1", "t5", "f8", "t11", "t12", "t21", "t23", "g32", "t46"]
    result = duplicate_message.solve(messages)
    print(f"Input: {messages}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()
