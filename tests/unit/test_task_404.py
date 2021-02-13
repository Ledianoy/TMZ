import pytest

from tasks.Lesson4.task404 import sum_cube


@pytest.mark.unit
def test_heppy():
    test_data = {
        1: 1,
        10: 3025,
        50: 1625625,
        100: 25502500,
    }

    for test_value, expected_value in test_data.items():
        value = sum_cube(test_value)
        assert expected_value == value

@pytest.mark.unit
def test_word():
    ok = False
    try:
        sum_cube("test")
    except ValueError:
        ok = True

    assert ok, "ne ok"