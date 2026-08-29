def divide(a: int, b: int) -> int:
    """
    Does division

    Args:
        a: Nominator
        b: Denominator
    
    Return:
        Returns the result a/b
    
    Returns ZeroDivisionError if b is 0.

    """

    try:
        c = a / b
        return c
    except:
        raise ZeroDivisionError

division = divide(4, 0)
print(division)