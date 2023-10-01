from username_generator import get_next_char
import numpy as np

np.random.seed(42) # for reproducibility purposes

class TestGetNextChar:
    def test_get_next_char_returns_string(self):
        start_char = 'a'
        transition_matrix = {'a': {'b': 0, 'c': 1}}

        assert type(get_next_char(transition_matrix, start_char) == str)
        
    def test_get_next_char_returns_from_lexicon(self):
        start_char = 'a'
        transition_matrix = {'a': {'b': 1}}

        assert get_next_char(transition_matrix, start_char) == 'b'
    
    def test_get_next_char_samples(self):
        start_char = 'a'
        transition_matrix = {'a': {'b': 4, 'c': 1}}

        assert get_next_char(transition_matrix, start_char) == 'b'
    