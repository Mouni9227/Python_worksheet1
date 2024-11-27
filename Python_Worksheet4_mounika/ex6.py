"""Check for the presence of a BisI restriction site using regular expression character groups:
A character group is a pair of square brackets with a list of characters inside them.
dna = "ATCGCGAATTCAC"
pattern = GCNGC, where N represents any base, i.e. A, T, G, C"""
import re
dna = "ATCGCGAATTCAC"
pattern = 'GC[ATGC]GC'
match=re.findall(pattern, dna)
if match:
    print('Matched sequence', match)
else:
    print('No match')
for match in re.finditer(pattern,dna):
    print(f"Found {match.group()} at position {match.start()} to {match.end()}")