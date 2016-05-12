# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import Sized, List
from shoppinglist.item import Item

class ShoppingList(Sized):
    def __init__(self) -> None:
        self.items = [] # type: List[Item]

    def __len__(self) -> int:
        return len(self.items)

    def add(self, item: Item) -> None:
        if item in self.items:
            raise ValueError("Item already in list")

        self.items.append(item)

    def remove(self, item: Item) -> None:
        self.items.remove(item)

    def get(self) -> List[Item]:
        return self.items.copy()

    def clear(self) -> None:
        self.items.clear()
