"""Download dna.txt from the usual code folder in my drive. The file contains a made up DNA sequence.
Predict the fragment lengths that we will get if we digest the sequence with two made up
restriction enzymes – AbcI, whose recognition site is ANT/AAT, and AbcII, whose recognition site is GCRW/TG.
The forward slashes (/) in the recognition sites represent the place where the enzyme cuts the DNA."""
import re

with open("dna.txt") as dna_seq:
    data=dna_seq.read().strip().upper()

AbcI=r"A[ATGC]T(?=AAT)"
AbcII=r"GC[AG][AT](?=TG)"
cuts=[]
#AbcI cut positions
cuts+= [m.start() +3 for m in re.finditer(AbcI,data)]

#AbcII cut positions
cuts+= [m.start()+5 for m in re.finditer(AbcII,data)]
cuts=sorted(cuts)

#fragment position
fragment_position=[0] +cuts + [len(data)]
fragment_len=[]
for i in range(len(fragment_position)-1):
    l=fragment_position[i+1]-fragment_position[i]
    fragment_len.append(l)
#fragment_len=[ fragment_position[i+1] - fragment_position[i]  for i in range(len(fragment_position) - 1)]

print("cut positions:",cuts)
print("fragment lengths:",fragment_len)

















