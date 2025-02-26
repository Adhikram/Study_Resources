import importlib
import os
from typing import Any
from Day1 import Day1


class AdventOfCode:
    def __init__(self, day: int):
        self.day = day
        self.input_file = f"ProblemSolving/AOC2024/inputs/day{day}.txt"

    def read_input(self) -> str:
        with open(self.input_file, "r") as file:
            return file.read().strip()

    def read_input_lines(self) -> list[str]:
        with open(self.input_file, "r") as file:
            return file.readlines()

    def solve(self) -> Any:
        # Dynamically import the solution class
        try:
            a = []
            b = []
            input = self.read_input_lines()
            for line in input:
                left = line.split("   ")[0]
                right = line.split("   ")[1].replace("\n", "")
                if line.startswith("//"):
                    continue
                else:
                    a.append(int(left))
                    b.append(int(right))
            solver = Day1()
            print(solver.solve2(a,b))
        except ImportError:
            return f"Solution for Day {self.day} not found"

def main():

    aoc = AdventOfCode(1)
    aoc.solve()


if __name__ == "__main__":
    main()
