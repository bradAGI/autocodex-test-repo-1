"""Command-line greeting utility with optional personalization."""

import argparse
from typing import Optional, Sequence


def build_parser() -> argparse.ArgumentParser:
    """Return a parser configured with the ``--name`` CLI option."""
    parser = argparse.ArgumentParser(description="Print a personalized greeting.")
    parser.add_argument(
        "--name",
        "-n",
        default="Codex automation",
        help="Name to include in the greeting.",
    )
    return parser


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Parse CLI arguments, including the optional ``--name`` value."""
    parser = build_parser()
    return parser.parse_args(argv)


def compose_greeting(name: str) -> str:
    """Return a greeting string tailored to the provided name."""
    return f"Hello {name}!"


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Parse arguments and print the personalized greeting."""
    args = parse_args(argv)
    print(compose_greeting(args.name))


if __name__ == "__main__":
    main()
