"""Take a DNA sequence and determine whether or not it contains any ambiguous bases
– i.e. any bases that are not A, T, G or C. If there are ambiguous bases,
print all ambiguous bases and their positions.
dna = "CGATNCGGAACGATC"
"""
import re
dna="CGATNCGGAACGATCM"
pattern='[^ ATGC]'
ambiguous_base=re.findall(pattern,dna)
if ambiguous_base:
    print(ambiguous_base)
else:
    print("No ambiguous bases")

for m in re.finditer(pattern,dna):
    print(f"ambiguous base {m.group()} found at position {m.start()}")
