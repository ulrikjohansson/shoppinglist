import pytest # type: ignore
from pytest import fixture # type: ignore
from shoppinglist.list import ShoppingList
from shoppinglist.item import Item

@fixture
def shoppinglist() -> ShoppingList:
    return ShoppingList()

@fixture
def item_base() -> Item:
    return Item("blah")
@fixture
def item(request) -> Item:
    import pdb #type: ignore
    #pdb.set_trace()
    return Item(name="Test")
@fixture
def item2() -> Item:
    return Item(name="Test2")

def test_add_item_to_list(shoppinglist: ShoppingList, item: Item):
    shoppinglist.add(item)
    assert len(shoppinglist) == 1

def test_add_2_items_to_list(shoppinglist: ShoppingList, item: Item, item2: Item):
    shoppinglist.add(item)
    shoppinglist.add(item2)
    assert len(shoppinglist) == 2

def test_remove_item_from_list(shoppinglist: ShoppingList):
    shoppinglist.add(item)
    shoppinglist.remove(item)

def test_get_item_from_list(shoppinglist: ShoppingList, item: Item):
    shoppinglist.add(item)
    assert shoppinglist[0] == item

def test_cannot_add_same_item_object_twice(shoppinglist: ShoppingList, item: Item):
    with pytest.raises(ValueError):
        shoppinglist.add(item)
        shoppinglist.add(item)

def test_returned_items_are_references(shoppinglist: ShoppingList, item: Item):
    shoppinglist.add(item)

    assert shoppinglist[0] is item

@pytest.mark.item_name(item_name="item")
def test_clear_items_from_list(shoppinglist: ShoppingList, item: Item, item2: Item):
    shoppinglist.add(item)
    shoppinglist.add(item2)
    shoppinglist.clear()
    assert len(shoppinglist) == 0
