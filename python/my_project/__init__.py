"""Template program that calls a function written in Rust."""

from my_project._lowlevel import hello

def main():
    """Entry point."""
    print(hello())
