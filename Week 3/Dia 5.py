sequences = [
    " atgcgt ",
    " ttaaac ",
    " cgttga "
]
clean_sequences = []
for sequence in sequences:
    clean_sequences.append(sequence.upper().strip())
print(clean_sequences)