# -*- coding: utf-8 -*-
from copy import deepcopy
from collections.abc import Sequence # type: ignore
from typing import List, Iterable
from shoppinglist.item import Item

class ShoppingList(Sequence):
    def __init__(self) -> None:
        self.items = [] # type: List[Item]

    def __iter__(self) -> Iterable:
        return iter(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, key: int) -> Item:
        return self.items[key]

    def add(self, item: Item) -> None:
        if item in self.items:
            raise ValueError("Item already in list")

        self.items.append(item)

    def remove(self, item: Item) -> None:
        self.items.remove(item)

    def clear(self) -> None:
        self.items.clear()
