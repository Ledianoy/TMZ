import pytest

from tasks.Lesson4.task402.task402 import handle_task_402

@pytest.mark.unit
def test_happy():
    result = handle_task_402("100")
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