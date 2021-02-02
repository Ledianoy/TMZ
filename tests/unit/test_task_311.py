import pytest

from tasks.lesson3.task311.task311 import solution


@pytest.mark.unit
def test_happy():
    result = solution("Ledovskiy@gmail.com")
    assert result == (2)

@pytest.mark.unit
def test_happy_2():
    result = solution("Ledovskiy@gmail.co")
    assert result == (1)

@pytest.mark.unit
def test_unhappy():
    ok_test = False
    try:
        solution("Ledovskiygmail.com")
    except ValueError:
        ok_test = True
    except Exception:
        pass
    assert ok_test, "test crashed with an error"