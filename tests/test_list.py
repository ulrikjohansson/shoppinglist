from pytest import fixture

@fixture
def shoppinglist():
    from shoppinglist.list import ShoppingList
    return ShoppingList()

def test_add_item_to_list(shoppinglist):
    shoppinglist.add("test")

def test_get_length_of_1_item_list(shoppinglist):
    shoppinglist.add("test")
    assert len(shoppinglist) == 1

def test_get_length_of_2_item_list(shoppinglist):
    shoppinglist.add("test")
    shoppinglist.add("test2")
    assert len(shoppinglist) == 2

def test_remove_item_from_list(shoppinglist):
    shoppinglist.add("test")
    shoppinglist.remove("test")

def test_get_items_from_list(shoppinglist):
    shoppinglist.add("test")
    assert shoppinglist.get() == ["test"]

def test_clear_items_from_list(shoppinglist):
    shoppinglist.add("test")
    shoppinglist.add("test2")
    shoppinglist.clear()
    assert len(shoppinglist) == 0
