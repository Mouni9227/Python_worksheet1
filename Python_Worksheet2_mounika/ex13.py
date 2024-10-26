"""Given a dictionary with a values list, extract the key whose value has the most unique values.
Input : test_dict = {"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
Output : "Best"
Explanation : 3 (max) unique elements, 9, 6, 5 of "Best"."""

test_dict={'gfg':[5,7,7,7,7],'is':[6,7,7,7],'Best':[9,9,6,5,5]}

maxi = 0
dict_val = []
for k, v in test_dict.items():
    unique_len = len(set(v))
    if unique_len > maxi:
        maxi = unique_len
        dict_val = [k] # Reset dict_val with new max
    elif unique_len == maxi:
        dict_val.append((k, unique_len))  # Add to dict_val if equal to max

print(dict_val)







# maxi=0
# dict_val=[(k, len(set(v))) for k,v in test_dict.items() if len(set(v)) > maxi and (maxi := len(set(v)))]
# print(dict_val)
#
# max_len = 0
# dict_val = [(k, len(set(v))) for k, v in test_dict.items() if len(set(v)) > max_len and (max_len := len(set(v)))]