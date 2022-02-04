from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Jonathan", "Thompson") == "Thompson; Jonathan"
    assert make_full_name("Juan-Camilo", "Cruz") == "Cruz; Juan-Camilo"
    assert make_full_name("David", "Smith-Jones") == "Smith-Jones; David"
    
def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Thompson; Jonathan") == "Thompson"
    assert extract_family_name("Cruz; Juan-Camilo") == "Cruz"
    assert extract_family_name("Smith-Jones; David") == "Smith-Jones"


def test_extrat_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Thompson; Jonathan") == "Jonathan"
    assert extract_given_name("Cruz; Juan-Camilo") == "Juan-Camilo"
    assert extract_given_name("Smith-Jones; David") == "David"


pytest.main(["-v", "--tb=line", "-rN", __file__])