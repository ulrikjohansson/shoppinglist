# *-* coding: utf-8 *-*

class Item:
    def __init__(self):
        self._checked = False # type: bool

    def is_checked(self) -> bool:
        return self._checked

    def check(self) -> None:
        self._checked = True

    def uncheck(self) -> None:
        self._checked = False
