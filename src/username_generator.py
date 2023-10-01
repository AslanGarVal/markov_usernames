from typing import Dict, List

import numpy as np
import json

START_TOKEN= '%'
END_TOKEN = '&'

def get_next_char(transition_matrix: Dict[str, Dict[str, List[int]]], char: str) -> str:
    frecuencies = transition_matrix[char]
    probabilities = [x / sum(frecuencies.values()) for x in frecuencies.values()]

    return np.random.choice(list(frecuencies.keys()), p = probabilities)



class UsernameGenerator:
    def __init__(self) -> None:
        self.frequency_matrix = {}

    def train(self, path_to_training_dataset: str) -> None:

        with open(path_to_training_dataset, 'r') as f:
            lines = f.readlines()

            for line in lines:
                username = line.split(',')[0]

                username = START_TOKEN + username + END_TOKEN

                for i in range(1, len(username)):
                    previous = username[i - 1]
                    current = username[i]

                    if previous not in self.frequency_matrix:
                        self.frequency_matrix[previous]= {}

                    if current not in self.frequency_matrix[previous]:
                        self.frequency_matrix[previous][current] = 1
                    else: 
                        self.frequency_matrix[previous][current] += 1

    def persist(self, path_to_persisted_model) -> None:
        with open(path_to_persisted_model, 'w') as f:
            json.dump(self.frequency_matrix, f)  

    def load(self, path_to_model) -> None: 
        with open(path_to_model, 'r') as f:
            self.frequency_matrix = json.load(f)           

    def generate_user_name(self) -> str:
        username = START_TOKEN # start token
        next = get_next_char(self.frequency_matrix, username)
        while next != END_TOKEN:
            username += next
            next = get_next_char(self.frequency_matrix, next)
        
        return username[1:] # remove START tokens