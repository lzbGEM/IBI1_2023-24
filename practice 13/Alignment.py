
import re
import pandas as pd

# Open and read the content of the "SLC6A4_HUMAN.fa" file into the variable "human".
with open("SLC6A4_HUMAN.fa", "r") as file_human:
    human = file_human.read()

# Open and read the content of the "SLC6A4_MOUSE.fa" file into the variable "mouse".
with open("SLC6A4_MOUSE.fa", "r") as file_mouse:
    mouse = file_mouse.read()

# Open and read the content of the "SLC6A4_RAT.fa" file into the variable "rat".
with open("SLC6A4_RAT.fa", "r") as file_rat:
    rat = file_rat.read()

# Load the "BLOSUM62.xlsx" file into a pandas DataFrame called "BLOSUM62" using the 'openpyxl' engine.
BLOSUM62 = pd.read_excel("BLOSUM62.xlsx", engine='openpyxl')

# Use a regular expression to find all sequences in the "human" string that do not start with ">"
# and join them into a single string for "seq1".
Seq1 = re.findall(r'^[^>].*', human, re.MULTILINE)#can read multilines at once
seq1 = ''.join(Seq1)

# Repeat the process for the "mouse" string to get "seq2".
Seq2 = re.findall(r'^[^>].*', mouse, re.MULTILINE)
seq2 = ''.join(Seq2)

# Repeat the process for the "rat" string to get "seq3".
Seq3 = re.findall(r'^[^>].*', rat, re.MULTILINE)
seq3 = ''.join(Seq3)

# Define a dictionary to map amino acids to their corresponding index in the BLOSUM62 matrix.
amino_index = {
    'C': 0, 'S': 1, 'T': 2, 'P': 3, 'A': 4, 'G': 5, 'N': 6, 'D': 7,
    'E': 8, 'Q': 9, 'H': 10, 'R': 11, 'K': 12, 'M': 13, 'I': 14, 'L': 15,
    'V': 16, 'F': 17, 'Y': 18, 'W': 19
}

# Calculate the distance and similarity between human and mouse sequences.
distance = 0
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        distance += 1
similarity = 1 - distance / len(seq1)

# Initialize an empty list to store the scores for each amino acid pair.
score_vector = []

# Iterate over the length of "seq1" and calculate the score for each pair of amino acids.
for i in range(len(seq1)):
    index1 = amino_index.get(seq1[i])  # Get the index for the amino acid in "seq1".
    index2 = amino_index.get(seq2[i])  # Get the index for the amino acid in "seq2".
    # Fetch the score from the BLOSUM62 DataFrame and append it to the score_vector list.
    score = BLOSUM62.loc[index1, seq2[i]]
    score_vector.append(score)

# Calculate the total alignment score by summing the scores in the score_vector list.
alignment_score = sum(score_vector)

# Print the alignment score and the percentage of identical amino acids between human and mouse SC6A4.
print(f"Human SC6A4 and mouse SC6A4: alignment score is {alignment_score} and identical amino acid percent is {similarity}")


#repeat
distance = 0
for i in range(len(seq1)):
    if seq1[i] != seq3[i]:
        distance += 1
similarity = 1 - distance / len(seq3)

score_vector = []
for i in range(len(seq1)):
    index1 = amino_index.get(seq1[i])
    index2 = amino_index.get(seq3[i])
    score = BLOSUM62.loc[index1, seq3[i]]
    score_vector.append(score)
        
alignment_score = sum(score_vector)
print(f"Human SC6A4  and rat SC6A4: alignment score is {alignment_score} and identical amino acid percent is {similarity}")


distance = 0
for i in range(len(seq3)):
    if seq3[i] != seq2[i]:
        distance += 1
similarity = 1 - distance / len(seq1)

score_vector = []
for i in range(len(seq1)):
    index3 = amino_index.get(seq3[i])
    index2 = amino_index.get(seq2[i])
    score = BLOSUM62.loc[index3, seq2[i]]
    score_vector.append(score)
        
alignment_score = sum(score_vector)
print(f"Mouse SC6A4 and rat SC6A4: alignment score is {alignment_score} and identical amino acid percent is {similarity}")