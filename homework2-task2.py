ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]}

# Увеличиваем универсальность кода, чтобы он работал для словаря любой длины: 

n = len(ids)
username_template = "blahblahblah"

# Создаём список списков данных для каждого юзера:
user_data = []
i = 1
while i <= n:
    username_template = "user" + str(i)
#    print(username_template) - for debug
    user_data.append(ids[username_template])
#    print(user_data[i-1]) - for debug
    i = i + 1

# Создаём глобальный список уникальных значений:
unique_list = []


# Функция, которая добавляет элементы списка данных конкретного юзера
# в список уникальных значений:
def uniqueDataAnalysis(current_data):

    i = 1
    while i <= len(current_data):
        if current_data[i-1] in unique_list:
            pass
        else:
            unique_list.append(current_data[i-1])
        i = i + 1
        

    return

j = 1

while j <= n:
    current_data = user_data[j-1]
    uniqueDataAnalysis(current_data)
    j = j + 1
print("Unique data list:")
print(unique_list)
print("Unique data list sorted asc:")
unique_list.sort()
print(unique_list)

# Интересно, почему не работает  print(unique_list.sort())  ???
