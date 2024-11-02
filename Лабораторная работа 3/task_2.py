# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=","):
    participants_list1 = group1.split(delimiter)
    participants_list2 = group2.split(delimiter)

    common_participants = list(set(participants_list1).intersection(participants_list2))

    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", common)



