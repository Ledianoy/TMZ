import pytest

from tasks.lesson3.task303 import task303


@pytest.mark.unit
def test():
    result = task303.solution("aaa bbb")
    assert result == "!bbb aaa!"


# @pytest.mark.unit
# def test_empty():
#     result = task303.solution("")
#     assert result == " "