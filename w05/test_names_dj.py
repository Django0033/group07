from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    '''
    Tests the make_full_name function from name.py

    Parameters: 
        none
    Return:
        none
    '''
    assert make_full_name('Eleazar', 'Pequeno') == 'Pequeno; Eleazar'
    assert make_full_name('Sally', 'Brown') == 'Brown; Sally'
    assert make_full_name('Gray', 'Gray') == 'Gray; Gray'


def test_extract_family_name():
    '''
    Tests the extract_family_name function from name.py

    Parameters: 
        none
    Return:
        none
    '''
    assert extract_family_name('Pequeno; Eleazar') == 'Pequeno'
    assert extract_family_name('Brown; Sally') == 'Brown'
    assert extract_family_name('Gray; Gray') == 'Gray'


def test_extract_given_name():
    '''
    Tests the extract_given_name function from name.py

    Parameters: 
        none
    Return:
        none
    '''
    assert extract_given_name('Pequeno; Eleazar') == 'Eleazar'
    assert extract_given_name('Brown; Sally') == 'Sally'
    assert extract_given_name('Gray; Gray') == 'Gray'


pytest.main(['-v', '--tb=line', '-rN', __file__])
