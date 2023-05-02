from collections import Counter
from tabulate import tabulate


def ngrams(seq, n):
	n_grams = [seq[i:i + n] for i in range(len(seq) - n + 1)]
	n_grams_counts = Counter(tuple(gram) for gram in n_grams)
	headers = [f"{n}-gram", "Count"]
	table_data = [(gram, count) for gram, count in n_grams_counts.items()]
	table = tabulate(table_data, headers=headers, tablefmt="fancy_grid")
	return table
