"""
Take a DNA sequence and determine whether or not it contains any ambiguous bases – i.e. any bases that are
not A, T, G or C. If there is a non ambiguous base, print the non ambiguous base
dna = "ATCGCGYAATTCAC"
"""
import re
dna = "ATCGCGYAATTCAC"
pattern='[^ ATGC]'
ambigous_base=re.findall(pattern, dna)
if ambigous_base:
    print(ambigous_base)
else:
    print("No ambiguous base found")

#to find position of non ambiguous base
for m in re.finditer(pattern,dna):
    print(f"Ambiguous base {m.group(0)} found at position {m.start()}")

#to replace ambiguous base
clean_dna = re.sub(pattern, "N", dna)
print("Cleaned DNA sequence:", clean_dna)
