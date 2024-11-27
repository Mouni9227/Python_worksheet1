"""Here's a complex pattern to identify full-length eukaryotic messenger RNA sequences
- ^AUG[AUGC]{30,1000}A{5,10}$    Can you describe in a few bullet points what matches will occur?"""
#1 ^: Asserts that the match must start at the beginning of the string.
#2 AUG: Matches the start codon, which initiates translation in mRNA.
#3 [AUGC]{30,1000}: Matches between 30 and 1000 nucleotides (A, U, G, or C) following the start codon. This represents the coding region of the mRNA.
#4 A{5,10}: Matches a polyadenylation tail (a sequence of 5 to 10 adenine nucleotides, "AAAAA...").
#5 $: Asserts that the match must end at the end of the string.