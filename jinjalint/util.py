import collections.abc


def flatten(l):
    """
    Deeply flattens an iterable.
    """
    for el in l:
        if (isinstance(el, collections.abc.Iterable) and
                not isinstance(el, (str, bytes))):
            yield from flatten(el)
        else:
            yield el
