# an example of using the PDM to create a custom class
# that works like a list
from collections.abc import Iterable


class StaticArray:
    def __init__(self, init_val, capacity=5):
        if isinstance(init_val, Iterable):
            self.items = list(init_val)
            self.capacity = len(self.items)
        else:
            self.items = [init_val] * capacity
            self.capacity = capacity

    def __repr__(self):
        return f"StaticArray({self.items})"

    def __str__(self):
        return f"StaticArray({self.items})"

    def __len__(self):
        return self.capacity

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, index):
        if index >= self.capacity or index < -self.capacity:
            raise IndexError("Index out of range")
        return self.items[index]

    def __setitem__(self, index, val):
        if index >= self.capacity or index < -self.capacity:
            raise IndexError("Index out of range")
        self.items[index] = val

    def __delitem__(self, index):
        raise NotImplementedError("StaticArray does not support deletion")


sa = StaticArray([1, "hi", 3.14, True])
len(sa)

42 in sa
"hi" in sa

sa[3]

sa[42] = "hello"
