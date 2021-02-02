import pytest

from tasks.lesson3.task310.task310 import solution


@pytest.mark.unit
def test_happy():
    result = solution("55,20")
    assert result == ({5: 3, 20: 2}, {10: 2})


@pytest.mark.unit
def test_unhappy():
    ok_test = False
    try:
        solution("bank,balarus")
    except ValueError:
        ok_test = True
    except Exception:
        pass
    assert ok_test, "test crashed with an error"