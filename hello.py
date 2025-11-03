"""Simple greeting CLI that personalizes its message."""

import argparse
from typing import Optional, Sequence


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser for this greeting script."""
    parser = argparse.ArgumentParser(description="Print a personalized greeting.")
    parser.add_argument(
        "--name",
        default="Codex automation",
        help="Name to include in the greeting.",
    )
    return parser


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Parse command-line arguments and return the resulting namespace."""
    parser = build_parser()
    return parser.parse_args(argv)


def compose_greeting(name: str) -> str:
    """Return the greeting text for the provided name."""
    return f"Hello {name}!"


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Parse CLI arguments and print a personalized greeting."""
    args = parse_args(argv)
    print(compose_greeting(args.name))


if __name__ == "__main__":
    main()
