import pytest

from tasks.Lesson4.task407 import whole_numbers_sum


@pytest.mark.unit
def test_heppy():

    test_data = {
        f"1_10": f"1-2-3-4-5-6-7-8-9-10-10",
        f"5_50": f"5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34-35-36-37-38-39-40-41-42-43-44-45-46-47-48-49-50-46",
    }

    for test_value, expected_value in test_data.items():
        value_key = test_value
        value_zn = value_key.split("_")
        value_n = value_zn[0]
        value_m = value_zn[1]
        value = whole_numbers_sum(value_n,value_m)
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
            whole_numbers_sum(test_value,expected_value)
        except ValueError:
            ok = True

    assert ok, "ne ok"