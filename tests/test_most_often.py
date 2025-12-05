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

def test_multiple_add_item():
    test_class = MostOften(["Banana"])
    test_class.add_new("Apple")
    test_class.add_new("Cherry")
    actual = test_class.starting_list
    expected = ["Banana", "Apple", "Cherry"]
    assert actual == expected

def test_no_clear_winner():
    test_class = MostOften(["apple", "cherry", "pineapple"])
    actual = test_class.get_most_often()
    expected = "no clear winner"
    assert actual == expected

def test_clear_winner_for_strings():
    test_class = MostOften(["apple", "cherry", "cherry", "pineapple"])
    actual = test_class.get_most_often()
    expected = "cherry"
    assert actual == expected

def test_clear_winner_for_multiple_unique_strings():
    test_class = MostOften(["apple", "pineapple", "cherry", "pineapple", "cherry", "pineapple"])
    actual = test_class.get_most_often()
    expected = "pineapple"
    assert actual == expected

def test_clear_winner_for_ints():
    test_class = MostOften([1,2,3,4,4])
    actual = test_class.get_most_often()
    expected = 4
    assert actual == expected

def test_clear_no_clear_winner_for_ints():
    test_class = MostOften([1,2,3,4])
    actual = test_class.get_most_often()
    expected = "no clear winner"
    assert actual == expected

def test_clear_winner_for_bools():
    test_class = MostOften([True, True, False])
    actual = test_class.get_most_often()
    expected = True
    assert actual == expected

def test_no_clear_winner_for_bools():
    test_class = MostOften([True, True, False, False])
    actual = test_class.get_most_often()
    expected = "no clear winner"
    assert actual == expected

def test_clear_winner_mixed_types():
    test_class = MostOften(["apple", "pineapple", "cherry", 1, 2, "pineapple", True, False, "cherry", "pineapple"])
    actual = test_class.get_most_often()
    expected = "pineapple"
    assert actual == expected