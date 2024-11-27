"""Test if a DNA sequence contains an EcoRI restriction site using regular expressions.
dna = "ATCGCGAATTCAC"
pattern = GAATTC
"""
import re
dna="ATCGCGAATTCAC"
pattern="GAATTC"
test=re.search(pattern,dna)
if test:
    print('site found')
else:
    print('site not found')

