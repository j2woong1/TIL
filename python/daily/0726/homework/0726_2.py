def count_blood(blood_lst):
    blood_dict = {}

    for blood in blood_lst:
        if blood_dict.get(blood):
            blood_dict[blood] += 1
        else:
            blood_dict[blood] = 1
    return blood_dict


print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB'
]))
