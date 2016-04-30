# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import TypeVar, Generic, Sized, List

T = TypeVar('T')

class ShoppingList(Generic[T], Sized):
    def __init__(self) -> None:
        self.items = [] # type: List[T]

    def __len__(self) -> int:
        return len(self.items)

    def add(self, item: T) -> None:
        self.items.append(item)

    def remove(self, item: T) -> None:
        self.items.remove(item)

    def get(self) -> List[T]:
        return deepcopy(self.items)

    def clear(self) -> None:
        self.items.clear()
