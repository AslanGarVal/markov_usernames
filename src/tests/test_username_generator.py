import pytest
import json 

from username_generator import UsernameGenerator

training_set_path = '../data/mock_users.csv'
model_path = '../model/model.json'

@pytest.fixture
def generator():
    generator = UsernameGenerator()
    generator.train(training_set_path)

    return generator

class TestUsernameGeneration:

    def test_training_fills_transition_matrix(self, generator):
        assert 'a' in generator.frequency_matrix.keys()

    def test_training_outputs_correct_frequencies(self, generator):
        assert generator.frequency_matrix == {'%': {'a': 1}, 'a': {'b': 1}, 'b': {'&': 1}}

    def test_output_is_a_string(self, generator):
        name = generator.generate_user_name()
        assert type(name) == str

    def test_output_contains_only_alphanumeric(self, generator):
        name = generator.generate_user_name()
        assert name.isalnum() == True

    def test_output_generatest_expected_username(self, generator):
        name = generator.generate_user_name()
        assert name == 'ab'

    def test_persisting_model_outputs_file(self, generator):
        generator.persist(model_path)

        with open(model_path, 'r') as f:
            model = json.load(f)

            assert model == {'%': {'a': 1}, 'a': {'b': 1}, 'b': {'&': 1}}