"""
Advent of Code [YEAR] - Day [XX]: [PUZZLE NAME]
https://adventofcode.com/[YEAR]/day/[XX]
"""

from helpers import get_input


def part1(data: str) -> int:
    """
    Solve part 1.

    Example:
        >>> part1("example\\ninput")
        2
    """
    lines = data.strip().split('\n')
    # TODO: Implement
    return 0


def part2(data: str) -> int:
    """
    Solve part 2.

    Example:
        >>> part2("example\\ninput")
        2
    """
    lines = data.strip().split('\n')
    # TODO: Implement
    return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    # Load input using helper
    data = get_input(1)  # TODO: Update day number

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
