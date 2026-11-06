"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Parse a pick-list quantity string and return a positive integer."""
    result = int(value.strip())
    if result <= 0:
        raise ValueError("quantity must be positive")
    return result
