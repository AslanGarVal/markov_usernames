from username_generator import UsernameGenerator

training_data = 'data/users.csv'
output_path = 'model/trained_model.json'
counts_data = 'model/counts.json'

model = UsernameGenerator()

#model.train(training_data)

#model.persist(output_path, counts_data)
model.load(output_path)

for _ in range(10):
    print(model.generate_user_name())