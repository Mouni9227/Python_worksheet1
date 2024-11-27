"""Write a regular expression to split the DNA string wherever we see a base that
isn't A, T, G or C. if the dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG", the output
should be ['ACT', 'GCAT', 'GCTACGT', 'ACGAT', 'CGA', 'TCG']"""

import re
dna="ACTNGCATRGCTACGTYACGATSCGAWTCG"
pattern='[ATGC]*'
bases=re.findall(pattern,dna)
result=[b for b in bases if b]
print(result)

#or
ptn=r'[^ATGC]'
output=re.split(ptn,dna)
print(output)

