import pytest

def test_set_in():
    months = {"Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"}
    assert "Aug" in months

def test_set_add():
    months = {"Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov"}
    months.add("Dec")
    assert months == {"Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"}

def test_set_remove():
    months = {"Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec", "Month13"}
    months.remove("Month13")
    assert months == {"Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"}

# negative
def test_str_change():
    testStr = "String"
    try:
        testStr[0] = "z"
    except TypeError:
        assert testStr[0] == "S"

def test_str_slice():
    testStr = "String"
    assert testStr[2:-2] == "ri"

@pytest.mark.parametrize("input, expected", [(0, "0"), (5, "5"), (9, "9")])
def test_str_index(input, expected):
    testString = "0123456789"
    assert testString[input] == expected
