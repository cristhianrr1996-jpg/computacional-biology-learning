dna_sequences = [
    "ATGCGTAA",
    "GGGCTA",
    "TTATGCC",
    "AACCAA"]

def gc_content(sequence):
    gc_total = sequence.count("GC")
    return gc_total
for seq in dna_sequences:
    print("Sequence:", seq)
    print("length:", len(seq))
    if "ATG" in seq:
        print("star codon found")
    else:
        print("codon not found")
    gc = gc_content(seq)
    print("GC content", gc)