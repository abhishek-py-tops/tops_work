# Write a Python program to check whether a list contains a sub list.


def contains_sublist(main_list, sub_list):
    if not sub_list:
        return True  
    sub_len = len(sub_list)
    for i in range(len(main_list) - sub_len + 1):
        if main_list[i:i + sub_len] == sub_list:
            return True
    return False

main = [1, 2, 3, 4, 5]
sub = [3, 4]

result = contains_sublist(main, sub)
print("Sublist found?" , result)
