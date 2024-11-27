"""Here's a DNA sequence with the bits that we want to extract in bold:
ACTGCATTATATCGTACGAAATTATACGCGCG
Extract the bits of the string that match the pattern (highlighted in bold(ATTATAT)(AAATTATA) using findall():"""
import  re
dna="ACTGCATTATATCGTACGAAATTATACGCGCG"
pattern='ATTATAT|AAATTATA'
extract=re.findall(pattern,dna)
print('Bits of strings matching the bold pattern',extract)

