import pytest

@pytest.mark.number
def test_type():
    assert type(1 + 2) is int

@pytest.mark.number
def test_add_int():
    assert 5 + 2 == 7

@pytest.mark.string
def test_string():
    assert 'u' in 'sun'
    
@pytest.mark.string
def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'

@pytest.mark.skip(reason='chwilowo off')
def test_add_string2():
    assert ('sunny' + 'day') == 'sunnyday'