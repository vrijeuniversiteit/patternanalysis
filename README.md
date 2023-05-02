# patternanalysis

[Open in Colab to run example code](https://colab.research.google.com/drive/1XCW6bo3RQLj8GVJLnlbCDqfIl8rs8JU9?usp=sharing)


Use the implementations the following way:

```python
from patternanalysis import entropy, maximal_entropy, entropy_between_transitions, transition_density_matrix, transition_probability_matrix, ngrams

data = [0, 1, 0, 0, 0, 3, 2, 0, 3]
print(f"Entropy: {entropy(data)}")
print(f"Entropy between transitions: {entropy_between_transitions(data)}")
print(f"Maximal possible entropy: {maximal_entropy(data)}")

data = [0, 1, 0, 3, 2, 0, 3]
print(f"Transition density matrix: {transition_density_matrix(data)}")

data = [0, 1, 0, 3, 2, 0, 3]
print(transition_probability_matrix(data))

data = [0, 1, 0, 3, 2, 0, 3]
number_grams = 2
print(ngrams(data, number_grams))
```
 
