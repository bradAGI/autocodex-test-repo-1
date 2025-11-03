"""Simple greeting CLI that personalizes its message."""

import argparse
from typing import Optional, Sequence


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the greeting CLI.

    Returns:
        argparse.ArgumentParser: Parser configured with the ``--name`` option.
    """
    parser = argparse.ArgumentParser(description="Print a personalized greeting.")
    parser.add_argument(
        "--name",
        "-n",
        default="Codex automation",
        help="Name to include in the greeting.",
    )
    return parser


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Extract CLI arguments for the greeting command.

    Args:
        argv: Custom argument list for testing; defaults to ``sys.argv``.

    Returns:
        argparse.Namespace: Parsed CLI arguments with the resolved name.
    """
    parser = build_parser()
    return parser.parse_args(argv)


def compose_greeting(name: str) -> str:
    """Compose the text shown to the user.

    Args:
        name: Person to greet.

    Returns:
        str: Greeting message tailored for ``name``.
    """
    return f"Hello {name}!"


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Run the CLI and emit the greeting.

    Args:
        argv: Custom argument list for testing; defaults to ``sys.argv``.
    """
    args = parse_args(argv)
    print(compose_greeting(args.name))


if __name__ == "__main__":
    main()
