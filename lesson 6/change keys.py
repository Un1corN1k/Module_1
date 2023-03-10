def change_key(dict1):
    new_dict = {}
    new_dict = {val: key for key, val in dict1.items()}
    return new_dict


def change_key2(dict2):
    new_dict = {}
    for key, val in dict2.items():
        new_dict[val] = key
    return new_dict

dict = {1:2,3:4}
print(change_key2(dict))