def checkio(*args: int | float):
    """Return the difference between the largest and smallest numbers in args."""
    if args:
        return max(args) - min(args)
    return 0
