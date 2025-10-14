def check_string_case(text):
    """
    Повертає рядок з описом регістру:
    - "Усі літери великі"
    - "Усі літери малі"
    - "Змішаний регістр"
    - "Помилка: очікувався рядок"
    """
    if not isinstance(text, str):
        return "Помилка: очікувався рядок"

    if text.isupper():
        return "Усі літери великі"
    elif text.islower():
        return "Усі літери малі"
    else:
        return "Змішаний регістр"


def to_uppercase_list(word):
    """
    Повертає список літер слова у верхньому регістрі.
    Якщо не рядок — повертає порожній список.
    """
    if not isinstance(word, str):
        return []
    return [ch.upper() for ch in word]
