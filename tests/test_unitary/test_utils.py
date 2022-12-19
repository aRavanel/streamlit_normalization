from src.utils_nlp import split_string

def test_split_string():
    assert split_string('this is') == ['this', 'is']