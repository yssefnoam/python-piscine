def ft_filter(_fun, _iter):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true."""
    x = [i for i in _iter if _fun(i)]
    for y in x:
        yield y
