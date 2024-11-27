"""Check for the presence of an AvaII recognition site, which can have two different sequences: GGACC and GGTCC. Use regular expressions.
dna = "ATCGCGAATTCAC"
pattern = GGACC and GGTCC
"""
import re
dna = "ATCGCGAATTCAC"
pattern = 'GG[AT]CC'
matches=re.findall(pattern,dna)
if matches:
    print('match found',matches)
else:
    print("No match")


# #OTHER VARIATIONS FOR PRACTICE PURPOSE
#
# dna="ATCGGACCCGAATTCACGGTCC"
# pattern='GG[AT]CC'
# #finds all matches and make it as a list in op
# match=re.findall('GG[AT]CC',dna)
# print(match)
#
#
# #count matches
# print(len(match))
#
#
# #start and end with
# for match in re.finditer(pattern,dna):
#     print(f'Found {match.group()} at position {match.start()} to {match.end()}')
# #Found GGACC at position 2 to 6
# #Found GGTCC at position 16 to 20
#
#
# # Allow G and C to vary for below dna seq
# dna = "ATCGGACCCGAATTCACGGTCCGGGCCGAACC"
# pattern = r"G[GA]ACC"
# print(re.search(pattern, dna))
# # Find matches
# matches = re.findall(pattern, dna)
# print("Matched sequences with variation:", matches) #['GGACC', 'GAACC']
#
#
# # Case-insensitive matching
# dna = "atcggacccgaattcacggtcc"
# pattern = r"GG[AT]CC"
# matches = re.findall(pattern, dna, re.IGNORECASE)
# print("Matched sequences (case-insensitive):", matches) #['ggacc', 'ggtcc']
#
#
# # Count specific occurrences
# if len(matches) == 1:
#     print("DNA contains exactly one target site:", matches[0])
# else:
#     print(f"DNA contains {len(matches)} target sites:", matches) #['GGACC', 'GGTCC']
#
#
# #Match sequences with variable length repeats:
# dna = "ATCGGAAAACCGAATTCAC"
# pattern = r"GG(A)+CC"
# matches = re.findall(pattern, dna)
# print("Matched sequences with variable repeats:", matches) #['AAA']
#
#
# #Match sequences with optional characters:
# # Find sequences like "GGACC" or "GGAC" (GGAC(C)?).
# dna = "ATCGGACCCGAATTGGACC"
# pattern = r"GGAC(C)?"
# matches = re.findall(pattern, dna)
# print("Matched sequences with optional characters:", matches) #[('C',), ('C',)]
#
#
# #Match overlapping patterns:
# # For "GGA" within "GGAA", ensure you capture both "GGA" and "GGAA".
# dna = "ATCGGAAGGACCGAATTCAC"
# pattern = r"(?=(GGA))"
# matches = re.findall(pattern, dna)
# print("Matched overlapping sequences:", matches) #['GGA', 'GGA']
#
#
# #Match sequences containing alternative middle regions:
# # "GGACC", "GGATC", or "GGAGC".
# dna = "ATCGGACCCGGATCCGGAGCC"
# pattern = r"GG(A|T|G)CC"
# matches = re.findall(pattern, dna)
# print("Matched sequences with alternatives:", matches) #['A', 'T', 'G']
#
#
# #Match sequences with nucleotide repeats:
# # Look for poly-A tails (e.g., "AAAAA").
# pattern = r"A{5,}"  # Match at least 5 consecutive 'A's
# dna = "ATCGAAATTTTCCCCAAAAATG"
# matches = re.findall(pattern, dna)
# print("Matched poly-A tails:", matches) #['AAAAA']






