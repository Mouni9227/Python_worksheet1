"""Here's a list of made up gene accession names:
accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
Write a program that will print only the accession names that satisfy the following criteria – treat each criterion separately:"""
import re
accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
#1.contain the number 5
ptn1=r'5'
match1=[i for i in accessions if re.search(ptn1,i)]
print(match1)

#2. contain the letter d or e
ptn2='d|e'
match2=[i for i in accessions if re.search(ptn2,i)]
print(match2)

#3. contain the letters d and e in that order
ptn3='d.*e'
match3=[i for i in accessions if re.search(ptn3,i)]
print(match3)

#4. contain the letters d and e in that order with a single letter between them
ptn4='d.e'
match4=[i for i in accessions if re.search(ptn4,i)]
print(match4)

#5. contain both the letters d and e in any order
ptn5='(?=.*d)(?=.*e)'
match5=[i for i in accessions if re.search(ptn5,i)]
print(match5)

#6. start with x or y
ptn6='^[xy]'
match6=[i for i in accessions if re.search(ptn6,i)]
print(match6)

#7. start with x or y and end with e
ptn7='^[xy].*e$'
match7=[i for i in accessions if re.search(ptn7,i)]
print(match7)

#8. contain three or more digits in a row
ptn8=r'\d{3,}'
match8=[i for i in accessions if re.search(ptn8,i)]
print(match8)

#9. end with d followed by either a, r or p
ptn9=r'd[arp]$'
match9=[i for i in accessions if re.search(ptn9,i)]
print(match9)