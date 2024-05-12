
import re
import blosum as bl
matrix = bl.BLOSUM(62)

# Open and read the content of the "SLC6A4_HUMAN.fa" file into the variable "human".
with open("SLC6A4_HUMAN.fa", "r") as file_human:
    human = file_human.read()

# Open and read the content of the "SLC6A4_MOUSE.fa" file into the variable "mouse".
with open("SLC6A4_MOUSE.fa", "r") as file_mouse:
    mouse = file_mouse.read()

# Open and read the content of the "SLC6A4_RAT.fa" file into the variable "rat".
with open("SLC6A4_RAT.fa", "r") as file_rat:
    rat = file_rat.read()


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




# Initialize the distance between the two sequences to be 0
distance = 0

# Loop through each position in seq1
for i in range(len(seq1)):
    # If the characters in seq1 and seq2 are different, add the distance
    if seq1[i] != seq2[i]:
        distance += 1
# Calculate the similarity 
similarity = 1 - distance / len(seq1)

# Initialize the score to be 0
score = 0
# Loop through each position in seq1 again
for i in range(len(seq1)):
    # Add the value from the matrix at the position corresponding to seq1[i] and seq2[i] to the score
    score += matrix[seq1[i]][seq2[i]]
# Print the alignment score and the percentage of identical amino acids between the two sequences
print(f"Human SC6A4 and mouse SC6A4: alignment score is {score} and identical amino acid percent is {similarity}")


#repeat
distance = 0
for i in range(len(seq1)):
    if seq1[i] != seq3[i]:
        distance += 1
similarity = 1 - distance / len(seq1)
score = 0
for i in range(len(seq1)):
    score += matrix[seq3[i]][seq1[i]]

print(f"Human SC6A4 and rat SC6A4: alignment score is {score} and identical amino acid percent is {similarity}")




distance = 0
for i in range(len(seq1)):
    if seq3[i] != seq2[i]:
        distance += 1
similarity = 1 - distance / len(seq1)
score = 0
for i in range(len(seq1)):
    score += matrix[seq3[i]][seq2[i]]

print(f"Mouse SC6A4 and rat SC6A4: alignment score is {score} and identical amino acid percent is {similarity}")





























# distance = 0
# for i in range(len(seq1)):
#     if seq1[i] != seq3[i]:
#         distance += 1
# similarity = 1 - distance / len(seq3)

# score_vector = []
# for i in range(len(seq1)):
#     index1 = amino_index.get(seq1[i])
#     index2 = amino_index.get(seq3[i])
#     score = BLOSUM62.loc[index1, seq3[i]]
#     score_vector.append(score)
        
# alignment_score = sum(score_vector)
# print(f"Human SC6A4  and rat SC6A4: alignment score is {alignment_score} and identical amino acid percent is {similarity}")


# distance = 0
# for i in range(len(seq3)):
#     if seq3[i] != seq2[i]:
#         distance += 1
# similarity = 1 - distance / len(seq1)

# score_vector = []
# for i in range(len(seq1)):
#     index3 = amino_index.get(seq3[i])
#     index2 = amino_index.get(seq2[i])
#     score = BLOSUM62.loc[index2, seq3[i]]
#     score_vector.append(score)
        
# alignment_score = sum(score_vector)
# print(f"Mouse SC6A4 and rat SC6A4: alignment score is {alignment_score} and identical amino acid percent is {similarity}")




