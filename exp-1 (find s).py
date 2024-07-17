training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]
def initialize_hypothesis(num_attributes):
    return ['0'] * num_attributes
def find_s_algorithm(training_data):
    num_attributes = len(training_data[0]) - 1
    hypothesis = initialize_hypothesis(num_attributes)
    hypotheses = [hypothesis.copy()]
    for example in training_data:
        if example[-1] == 'Yes':
            for i in range(num_attributes):
                if hypothesis[i] == '0':
                    hypothesis[i] = example[i]
                elif hypothesis[i] != example[i]:
                    hypothesis[i] = '?'
            hypotheses.append(hypothesis.copy())   
    return hypothesis, hypotheses

most_specific_hypothesis, all_hypotheses = find_s_algorithm(training_data)
print("The most specific hypothesis found by FIND-S is:")
print(most_specific_hypothesis)
print("\nAll hypotheses encountered during the learning process:")
for i, hyp in enumerate(all_hypotheses):
    print(f"Hypothesis {i}: {hyp}")
