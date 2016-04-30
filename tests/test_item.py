from pytest import fixture

@fixture
def item():
    from shoppinglist.item import Item
    return Item()

def test_default_state_is_unchecked(item):
    assert item.is_checked() is False

def test_checking_item_marks_it_as_checked(item):
    item.check()
    assert item.is_checked() is True

def test_unchecking_a_checked_item_marks_it_as_unchecked(item):
    item.check()
    item.uncheck()
    assert item.is_checked() is False
