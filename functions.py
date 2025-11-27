def check_string_case(text):
    if not isinstance(text, str):
        return "Помилка: очікувався рядок"

    if text.isupper():
        return "Усі літери великі"
    elif text.islower():
        return "Усі літери малі"
    else:
        return "Змішаний регістр"
