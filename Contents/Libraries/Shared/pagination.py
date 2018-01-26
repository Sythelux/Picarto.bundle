import itertools


class PaginationStore(object):
    def __init__(self):
        self.online_pages = None  # type list

    @staticmethod
    def grouper(n, iterable, fillvalue=None):
        """grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"""
        args = [iter(iterable)] * n
        return itertools.izip_longest(fillvalue=fillvalue, *args)


# val = PaginationStore.grouper(3, (3, 34, 5, 6, 3, 2, 454, 645, 34))
# print(type(val))
# print(str(list(val)))
