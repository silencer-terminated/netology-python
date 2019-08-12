queries = [
"смотреть сериалы онлайн",
"новости спорта",
"афиша кино",
"курс доллара",
"сериалы этим летом",
"курс по питону",
"сериалы про спорт",
"I'm blue da ba dee da ba dai",
]

def percentage(queries):


    # Простая защита от дурака
    if len(queries) <= 0:
        print("Your data input is wrong, pease check it")
        raise SystemExit


    # Находим максимальное количество слов в запросе:
    i = 0
    max_words = 0
    word_count = []

    while i < len(queries):

        query_element = queries[i]
        spaces_count = query_element.count(" ")
        if max_words < spaces_count:
            max_words = spaces_count
            
        i = i + 1
        
    max_words = max_words + 1
    print("Max query length, words:", max_words)



    # Создаём бланк списка встречаемости запросов из разного кол-ва слов.
    # NB! Нулевой элемент - количество запросов с ОДНИМ словом.
    i = 0
    while i < max_words:
        word_count.append(0)
        i = i + 1

    # print("Counter list template:", word_count) - for debug


    # Считаем общее кол-во запросов и кол-во запросов разной длины в словах:
    i = 0
    total_queries = 0
    while i < len(queries):
        query_element = queries[i]
        spaces_count = query_element.count(" ")
        word_count[spaces_count] = word_count[spaces_count] + 1
        total_queries = total_queries + 1
        i = i + 1

    # print(total_queries) - for debug


    i = 0
    while i < max_words:
        print("Amount of queries consisting of", i + 1, "word(s) is:", round(((word_count[i] / total_queries)* 100), 2), "%")
        i = i + 1

    return

percentage(queries)
