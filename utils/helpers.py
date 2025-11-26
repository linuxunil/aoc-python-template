"""Helper functions for Advent of Code solutions."""


def get_input(day: int) -> str:
    """
    Read input file for a specific day.

    Args:
        day: Day number (1-25)

    Returns:
        Input data as a string

    Example:
        >>> # Reads from inputs/01.txt
        >>> data = get_input(1)  # doctest: +SKIP
    """
    filename = f"inputs/{day:02d}.txt"
    with open(filename) as f:
        return f.read()
