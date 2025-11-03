"""Simple greeting CLI that personalizes its message."""

import argparse
from typing import Optional, Sequence


def build_parser() -> argparse.ArgumentParser:
    """Build and configure the CLI argument parser.

    Returns:
        argparse.ArgumentParser: Parser with arguments defined for the script.
    """
    parser = argparse.ArgumentParser(description="Print a personalized greeting.")
    parser.add_argument(
        "--name",
        default="Codex automation",
        help="Name to include in the greeting.",
    )
    return parser


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Parse the command-line arguments for the greeting script.

    Args:
        argv: Custom argument list for testing; defaults to ``sys.argv``.

    Returns:
        argparse.Namespace: Parsed CLI arguments.
    """
    parser = build_parser()
    return parser.parse_args(argv)


def compose_greeting(name: str) -> str:
    """Compose a personalized greeting.

    Args:
        name: Person to greet.

    Returns:
        str: Greeting message.
    """
    return f"Hello {name}!"


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Program entry point for the greeting script.

    Args:
        argv: Custom argument list for testing; defaults to ``sys.argv``.
    """
    args = parse_args(argv)
    print(compose_greeting(args.name))


if __name__ == "__main__":
    main()
