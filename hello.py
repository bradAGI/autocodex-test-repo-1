"""Simple greeting CLI that personalizes its message."""

import argparse


def main() -> None:
    """Parse CLI arguments and print a personalized greeting."""
    parser = argparse.ArgumentParser(description="Print a personalized greeting.")
    parser.add_argument(
        "--name",
        default="Codex automation",
        help="Name to include in the greeting.",
    )
    args = parser.parse_args()
    print(f"Hello {args.name}!")


if __name__ == "__main__":
    main()
