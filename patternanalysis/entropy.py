from collections import Counter


def entropy(data):
	import math
	n = len(data)
	counts = Counter(data)
	probs = [float(c) / n for c in counts.values()]
	entropy = 0
	for p in probs:
		if p > 0.0:
			entropy -= p * math.log(p, 2)
	entropy = round(entropy, 2)
	return entropy


def entropy_between_transitions(data):
	import math
	n = len(data)
	modified_data = []
	for i in range(1, n):
		if data[i] != data[i - 1]:
			modified_data.append(data[i])
	counts = Counter(modified_data)
	probs = [float(c) / len(modified_data) for c in counts.values()]
	entropy = 0
	for p in probs:
		if p > 0.0:
			entropy -= p * math.log(p, 2)

	entropy = round(entropy, 2)
	return entropy


def maximal_entropy(data):
	num_states = len(set(data))
	import math
	probs = [1.0 / num_states] * num_states
	entropy = 0
	for p in probs:
		if p > 0.0:
			entropy -= p * math.log(p, 2)
	return entropy


# calculate number of states in data (set)
def _num_states(data):
	return len(set(data))
