data = [0, 1, 0, 1, 0, 2, 0, 1, 0]

def lempel_ziv_complexity(seq):
    substrings = []
    i = 0
    while i < len(seq):
        j = i + 1
        while j <= len(seq):
            substr = seq[i:j]
            if substr not in substrings:
                substrings.append(substr)
            j += 1
        i += 1
    return len(substrings)


print(lempel_ziv_complexity(data))
