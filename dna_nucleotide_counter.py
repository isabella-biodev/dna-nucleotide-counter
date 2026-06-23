# Bioinformatics Project - Count nucleotides in a DNA sequence using dictionaries, loops and conditionals

dna = input("Enter a DNA sequence:").upper()
counts = {
    "A": 0,
    "T": 0,
    "G": 0,
    "C": 0
}

for nucleotide in dna:
    if nucleotide in counts:
        counts[nucleotide] += 1
    else:
        print(f"Warning: Unknown nucleotide detected: {nucleotide}")
print("\nNucleotide counts")
print(counts)

#dna = input("Enter a DNA sequence:").upper()





























