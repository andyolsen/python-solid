import pytest
from util import get_grade

@pytest.mark.parametrize("mark, grade", [
    (99, "A*"),
    (70, "A"),
    (69, "B"),
    (60, "B"),
    (59, "C"),
    (50, "C"),
    (49, "D"),
    (40, "D"),
    (39, "E"),
    (30, "E"),
    (29, "U")
])
def test_marks_and_grades(mark, grade):
    assert grade == get_grade(mark)