users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

visits = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
count_of_visits = len(users)
visits["Общее количество"] = count_of_visits
count_of_unique_visits = len(set(users))
visits["Уникальные посещения"] = count_of_unique_visits

print(visits)
