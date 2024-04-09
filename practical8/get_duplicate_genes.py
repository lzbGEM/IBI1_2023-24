
import re
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r', encoding="UTF-8") as f:
    a=f.read()
    names=re.findall(r"gene:(\S+).*duplication",a)#Find the gene names with the word duplication in the description section
    seqs = re.findall(r'duplication.+\n((?:[^>].*\n)+)', a)#Find the string that does not begin with > immediately after the line break that contains duplication
    dict = {name: seq for name, seq in zip(names, seqs)}#Dictionary generation simplifies the code, here zip makes the two lists correspond one to one
    output_str = ""
    for key, value in dict.items():
        output_str += f"{key}\n{value}\n\n"#Output the contents of the dictionary as a string
with open('duplicate_genes.fa', 'w', encoding="UTF-8") as output_file:#Write it in a new file
    output_file.write(output_str)
with open('duplicate_genes.fa', 'r', encoding="UTF-8") as output_file:
    print(output_file.read())



    



    
    





    
    









