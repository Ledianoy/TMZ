import pytest

from tasks.Lesson4.task406 import sum_cube


@pytest.mark.unit
def test_heppy():

    test_data = {
        f"1_10": 2025,
        f"5_50": 1500525,
    }

    for test_value, expected_value in test_data.items():
        value_key = test_value
        value_zn = value_key.split("_")
        value_n = value_zn[0]
        value_m = value_zn[1]
        value = sum_cube(value_n,value_m)
        assert expected_value == value

@pytest.mark.unit
def test_word():
    test_data = {
        "1":"1",
        "2": "test",
        "test": "1",
        "test2" : "test2",
    }
    ok = False
    for test_value, expected_value in test_data.items():
        try:
            sum_cube(test_value,expected_value)
        except ValueError:
            ok = True

    assert ok, "ne ok"