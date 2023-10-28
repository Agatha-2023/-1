def find_common_participants(str_1, str_2, DEFAULT_SEP = ','):
    group_1 = str_1.split(DEFAULT_SEP)
    group_2 = str_2.split(DEFAULT_SEP)
    common_participants = list(set(group_1).intersection(set(group_2)))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
