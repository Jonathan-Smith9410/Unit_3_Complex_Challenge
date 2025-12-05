from lib.most_often import *

def test_instantiate_class():
    test_class = MostOften([])
    actual = test_class.starting_list
    expected = []
    assert actual == expected

def test_add_item():
    test_class = MostOften([])
    test_class.add_new("Apple")
    actual = test_class.starting_list
    expected = ["Apple"]
    assert actual == expected