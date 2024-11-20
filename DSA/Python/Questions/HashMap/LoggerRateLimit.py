"""
# Question: Logger Rate Limiter
# Link: https://leetcode.com/problems/logger-rate-limiter/

# Time Complexity: O(1)
# Space Complexity: O(n)

# Algorithm:
# 1. Track message timestamps in dictionary
# 2. Check if message can be printed
# 3. Update timestamp for next allowed print
"""


class LoggerRateLimit:
    def __init__(self):
        self.store = {}

    def should_print_message(self, timestamp: int, message: str) -> bool:
        allowed_timestamp = self.store.get(message, 0)
        if allowed_timestamp <= timestamp:
            self.store[message] = timestamp + 10
            return True
        return False


def main():
    logger = LoggerRateLimit()
    print(logger.should_print_message(1, "foo"))  # True
    print(logger.should_print_message(2, "bar"))  # True
    print(logger.should_print_message(3, "foo"))  # False
    print(logger.should_print_message(8, "bar"))  # False
    print(logger.should_print_message(10, "foo"))  # False
    print(logger.should_print_message(11, "foo"))  # True


if __name__ == "__main__":
    main()
