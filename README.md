# Advent of Code 2024 - Python Template

Template repository for solving Advent of Code puzzles in Python. Features automatic input downloading, integrated testing with doctests, and task automation with mise.

## Features

- **uv** for fast Python package management
- **aocd** for automatic input downloading from adventofcode.com
- **Doctests** for inline example testing
- **Mise tasks** for workflow automation
- **Separate input/solution directories** for clean organization

## Prerequisites

Install mise and uv:

```bash
# Install mise (https://mise.jdx.dev/)
curl https://mise.run | sh

# Install uv (https://docs.astral.sh/uv/)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup

1. **Clone or fork this repository**

2. **Get your Advent of Code session token:**
   - Log in to https://adventofcode.com
   - Open browser developer tools (F12)
   - Go to Application > Storage > Cookies
   - Copy the value of the `session` cookie

3. **Configure environment:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set your session token:
   ```
   AOC_SESSION=your_session_token_here
   AOC_YEAR=2024
   ```

4. **Initialize the project:**
   ```bash
   mise install    # Install Python 3.12
   uv sync         # Install dependencies
   ```

## Usage

### Daily Workflow

#### Start a new day (recommended):
```bash
mise day -- 1
```
This command:
- Downloads input to `inputs/01.txt`
- Creates `solutions/day01.py` from template
- Shows the challenge URL

#### Manual workflow:
```bash
# Download today's input (and any missing previous days)
uv run download_input.py

# Copy template for a specific day
cp template_day.py solutions/day05.py
```

### Solving Puzzles

1. **Open your solution file** (e.g., `solutions/day01.py`)

2. **Add example inputs to doctests** (from puzzle description):
   ```python
   def part1(data: str) -> int:
       \"\"\"
       Example:
           >>> part1("1\\n2\\n3")
           6
       \"\"\"
       # Your solution here
   ```

3. **Run tests:**
   ```bash
   mise test
   ```

4. **Implement your solution** until tests pass

5. **Run with real input:**
   ```bash
   mise solve -- 1
   ```

6. **Submit answer** manually on https://adventofcode.com

### Mise Tasks

```bash
mise day -- 5    # Setup day 5 (download input + create solution)
mise test        # Run all tests (doctests)
mise solve -- 5  # Run solution for day 5
```

## Project Structure

```
.
├── .mise.toml           # Mise task configuration
├── pyproject.toml       # Python project and dependencies
├── .env                 # Your session token (git-ignored)
├── .env.example         # Template for .env
├── download_input.py    # Bulk download script
├── helpers.py           # Input loading helper
├── template_day.py      # Template for new days
├── inputs/              # Downloaded inputs (git-ignored)
│   ├── 01.txt
│   └── 02.txt
└── solutions/           # Your solutions
    ├── day01.py
    └── day02.py
```

## Writing Solutions

Each day's solution follows this pattern:

```python
\"\"\"
Advent of Code 2024 - Day 1: Puzzle Name
https://adventofcode.com/2024/day/1
\"\"\"

from helpers import get_input


def part1(data: str) -> int:
    \"\"\"
    Solve part 1.

    Example:
        >>> part1("example\\ninput")
        42
    \"\"\"
    lines = data.strip().split('\\n')
    # Your solution here
    return 0


def part2(data: str) -> int:
    \"\"\"
    Solve part 2.

    Example:
        >>> part2("example\\ninput")
        84
    \"\"\"
    lines = data.strip().split('\\n')
    # Your solution here
    return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    data = get_input(1)  # Update day number
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
```

### Tips

- **Use doctests** - Add examples from puzzle descriptions to catch errors early
- **Keep functions pure** - `part1()` and `part2()` should only take data as input
- **Use helper function** - `get_input(day)` reads from `inputs/XX.txt`
- **Test incrementally** - Run `mise test` frequently while developing
- **Read the whole input** - Many puzzles have subtle details in the full input

## Bulk Download

To download all available inputs at once (useful for catching up):

```bash
uv run download_input.py
```

This downloads all inputs from day 1 to today (or day 25 if not December).

## Forking for Next Year

1. Fork or clone this repository
2. Update `AOC_YEAR=2025` in `.env`
3. Clear `solutions/` directory (keep `__init__.py`)
4. Clear `inputs/` directory (keep `.gitkeep`)
5. Update year in README title
6. Start solving!

## Troubleshooting

**"No module named 'aocd'"**
- Run `uv sync` to install dependencies

**"Puzzle inputs differ by user"**
- Make sure your `AOC_SESSION` is set correctly in `.env`
- Get a fresh token from your browser cookies

**"Can't download input"**
- Puzzle inputs aren't available until midnight EST (UTC-5)
- Check that you're logged in to adventofcode.com

**Mise tasks not working**
- Make sure `.env` file exists with your session token
- Try running `mise install` again

## License

Template code is public domain. Your solutions are yours!

Happy coding! 🎄
