# noqa: D207, D209, D400
"""Recode the built-in filter function as a lazy generator."""


def ft_filter(function, iterable):
    # La docstring ci-dessous n'est volontairement pas formatée selon
    # la norme PEP257 : le sujet exige qu'elle soit strictement
    # identique à filter.__doc__ (voir ft_filter.__doc__ == filter.__doc__).
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item
