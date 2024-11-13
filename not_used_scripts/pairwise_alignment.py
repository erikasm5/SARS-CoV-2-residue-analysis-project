from Bio import pairwise2

# Define your three sequences
seq1 = "CPFGEVFNATKFPSVYAWERKKISNCVADYSVLYNSTFFSTFKCYGVSATKLNDLCFSNVYADSFVVKGDDVRQIAPGQTGVIADYNYKLPDDFMGCVLAWNTRNIDATSTGNYNYKYRLFRKSNLKPFERDISTEIYQAGSTPCNGVAGFNCYFPLRSYSFRPTYGVGHQPYRVVVLSFELT-----VCG"
seq2 = "CPFHEVFNATTFASVYAWNRKRISNCVADYSVIYNFAPFFAFKCYGVSPTKLNDLCFTNVYADSFVIRGNEVSQIAPGQTGNIADYNYKLPDDFTGCVIAWNSNKLDSKPSGNYNYLYRLFRKSKLKPFERDISTEIYQAGNRPCNGVAGPNCYSPLQSYGFRPTYGVGHQPYRVVVLSFELLHAPATVCG"
seq3 = "CPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCG"



# Perform pairwise sequence alignments
alignments12 = pairwise2.align.globalxx(seq1, seq2)
alignments13 = pairwise2.align.globalxx(seq1, seq3)
alignments23 = pairwise2.align.globalxx(seq2, seq3)

# Print the alignment scores and aligned sequences
print("Alignment 1-2 score:", alignments12[0][2])
print(pairwise2.format_alignment(*alignments12[0]))

print("Alignment 1-3 score:", alignments13[0][2])
print(pairwise2.format_alignment(*alignments13[0]))

print("Alignment 2-3 score:", alignments23[0][2])
print(pairwise2.format_alignment(*alignments23[0]))
