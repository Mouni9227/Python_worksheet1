"""Write a regular expression to extract the genus name and species name into separate variables.
For example, if scientific_name = "Homo sapiens", the output should be genus is Homo, species is sapiens.
Test your program with another example of scientific_name = “Drosophila melanogaster”."""
import re
names=["Homo sapiens","Drosophila melanogaster"]
pattern=r"^(\w+)\s+(\w+)$"
for scientific_name in names:
    match=re.match(pattern,scientific_name)
    if match:
        genus=match.group(1)
        species=match.group(2)
        print(f"Scientific name: {scientific_name}")
        print(f"Genus: {genus}")
        print(f"Species: {species}\n")
    else:
        print(f"Invalid scientific name: {scientific_name}")


# #OTHER VARIATIONS
# #1. Using Word Boundaries (\b)
# import re
#
# # Test examples
# names = ["Homo sapiens", "Drosophila melanogaster"]
#
# # Regular expression with word boundaries
# pattern = r"\b(\w+)\b\s+\b(\w+)\b"
#
# for scientific_name in names:
#     match = re.search(pattern, scientific_name)
#     if match:
#         genus, species = match.group(1), match.group(2)
#         print(f"Genus: {genus}, Species: {species}")
#     else:
#         print(f"Invalid scientific name: {scientific_name}")
#
#
# # 2. Matching Capitalized Genus
# import re
#
# # Regular expression enforcing capitalized genus
# pattern = r"^([A-Z][a-z]+)\s+([a-z]+)$"
#
# for scientific_name in names:
#     match = re.match(pattern, scientific_name)
#     if match:
#         genus, species = match.group(1), match.group(2)
#         print(f"Genus: {genus}, Species: {species}")
#     else:
#         print(f"Invalid scientific name: {scientific_name}")
#
#
#
# #3. Using Named Groups
# import re
#
# # Regular expression with named groups
# pattern = r"^(?P<genus>[A-Z][a-z]+)\s+(?P<species>[a-z]+)$"
#
# for scientific_name in names:
#     match = re.match(pattern, scientific_name)
#     if match:
#         genus = match.group("genus")
#         species = match.group("species")
#         print(f"Genus: {genus}, Species: {species}")
#     else:
#         print(f"Invalid scientific name: {scientific_name}")
#
#
# #4. Allowing Multiple Words for Species
# import re
#
# # Allow multi-word species names
# pattern = r"^([A-Z][a-z]+)\s+(.+)$"
#
# names = ["Homo sapiens", "Canis lupus familiaris"]
#
# for scientific_name in names:
#     match = re.match(pattern, scientific_name)
#     if match:
#         genus, species = match.group(1), match.group(2)
#         print(f"Genus: {genus}, Species: {species}")
#     else:
#         print(f"Invalid scientific name: {scientific_name}")
#
#
# #5. Using Non-Whitespace Characters
# import re
#
# # General regex using non-whitespace characters
# pattern = r"^(\S+)\s+(\S+)$"
#
# for scientific_name in names:
#     match = re.match(pattern, scientific_name)
#     if match:
#         genus, species = match.group(1), match.group(2)
#         print(f"Genus: {genus}, Species: {species}")
#     else:
#         print(f"Invalid scientific name: {scientific_name}")
#
#
# #6. Supporting Genus Abbreviation
# import re
#
# # Support genus abbreviation
# pattern = r"^([A-Z][a-z]*\.?)\s+([a-z]+)$"
#
# names = ["Homo sapiens", "H. sapiens", "Drosophila melanogaster"]
#
# for scientific_name in names:
#     match = re.match(pattern, scientific_name)
#     if match:
#         genus, species = match.group(1), match.group(2)
#         print(f"Genus: {genus}, Species: {species}")
#     else:
#         print(f"Invalid scientific name: {scientific_name}")
#
#
# #7. Extract All Parts of a Full Scientific Name
# import re
#
# # Full scientific name including subspecies
# pattern = r"^([A-Z][a-z]+)\s+([a-z]+)(?:\s+([a-z]+))?$"
#
# names = ["Canis lupus familiaris", "Homo sapiens"]
#
# for scientific_name in names:
#     match = re.match(pattern, scientific_name)
#     if match:
#         genus = match.group(1)
#         species = match.group(2)
#         subspecies = match.group(3) if match.group(3) else "N/A"
#         print(f"Genus: {genus}, Species: {species}, Subspecies: {subspecies}")
#     else:
#         print(f"Invalid scientific name: {scientific_name}")
#
# """
# Summary of Techniques:
#     Simple Matching: ^(\w+)\s+(\w+)$
#     Strict Capitalization: ^([A-Z][a-z]+)\s+([a-z]+)$
#     Named Groups: ^(?P<genus>[A-Z][a-z]+)\s+(?P<species>[a-z]+)$
#     Multi-word Species: ^([A-Z][a-z]+)\s+(.+)$
#     Abbreviated Genus: ^([A-Z][a-z]*\.?)\s+([a-z]+)$
#     Subspecies Support: ^([A-Z][a-z]+)\s+([a-z]+)(?:\s+([a-z]+))?$
# """

