# *-* coding: utf-8 *-*
from typing import *

class Item:
    def __init__(self, name: str, checked: bool = False) -> None:
        self._checked = checked # type: bool
        self._name = name # type: str

    def is_checked(self) -> bool:
        return self._checked

    def check(self) -> None:
        self._checked = True

    def uncheck(self) -> None:
        self._checked = False

    def __str__(self):
        checked = ("\u2611" if self.is_checked() else "\u2610")
        return "{checked} {name}".format(name=self._name, checked=checked)

#    def __repr__(self):
#        return "id:{obj_id!r} name:{name!r} checked:{checked!r}".format(obj_id=id(self), name=self._name, checked=self._checked)
