import pytest


@pytest.mark.numtest
def test_add_numbers():
	assert 3 + 4 == 7


@pytest.mark.numtest
def test_multiply_numbers():
	assert 3 * 4 == 12


@pytest.mark.strtest
def test_concatenate_strings():
    assert "hello " + "world" == "hello world"


@pytest.mark.strtest
def test_uppercase_strings():
    assert "hello world".upper() == "HELLO WORLD"