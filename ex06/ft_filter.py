import sys

def ft_filter(function, iterable: any) -> any:
    __doc__ = """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
    if function is None:
        return [element for element in iterable if element]
    else:
        return [element for element in iterable if function(element)]
