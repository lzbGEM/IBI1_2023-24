
import re

def count_repeats(seq, repeat):
    count = 0
    start = 0
    while True:
        start = seq.find(repeat, start)
        if start == -1:
            break
        else:
            count += 1
            start += 1 
    return count

# Ask the user for input on which repeat sequence to look for
file_name = input("Please input the repeat sequence (e.g., GTGTGT or GTCTGT): ")
new_file_name = f'{file_name}_duplicate_genes.fa'

# Read the input file and extract gene names and sequences with 'duplication'
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r', encoding="UTF-8") as f:
    a = f.read()
    names = re.findall(r"gene:(\S+).*duplication", a)  # Find the gene names with the word duplication in the description section
    seqs = re.findall(r'duplication.+\n((?:[^>].*\n)+)', a)  # Find the string that does not begin with > immediately after the line break that contains duplication
    dict = {name: seq for name, seq in zip(names, seqs)}  # Dictionary generation simplifies the code, here zip makes the two lists correspond one to one


with open(new_file_name, 'w', encoding="UTF-8") as output_file:
    for key, value in dict.items():
        # Remove all newline characters from the sequence and count the repeats
        seq_without_newlines = re.sub(r'\n', '', value)
        repeat_count = count_repeats(seq_without_newlines, file_name)
        # Write the gene name and sequence with the repeat count to the output file, all on a single line
        output_file.write(f">{key} (Repeat Count: {repeat_count})\n {seq_without_newlines}\n")

# Read and print the contents of the new file
with open(new_file_name, 'r', encoding="UTF-8") as output_file:
    print(output_file.read())



