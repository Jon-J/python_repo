"""
Multiple_inheritance: Define a class with more than one base class

 -  Subclass inherit methods of all bases
 -  Without conflict, names resolve in the obvious way
 -  Method Resolution Order(MRO) determines name lookup in all the classes
"""

class SimpleList:
    def __init__(self, items):
        self._items= items

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)

class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))


class IntList(SimpleList):
    def __init__(self, _items=()):
        for x in _items: self._validate(x)
        super().__init__(_items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('Intlist only supports integer values')

    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "Intlst {}".format(list(self))


class SortedIntlist(IntList, SortedList):
    def __repr__(self):
        return 'SortedIntList {}'.format(self)

sil = SortedIntlist([1,2,3])
sil.add(4)
sil.add('5')
print(sil.__repr__())
