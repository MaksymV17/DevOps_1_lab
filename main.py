from feature.functions import check_string_case, to_uppercase_list
from feature.generator import even_odd_generator

def main():
    # Просимо слово в користувача
    word = input("Введіть слово: ").strip()

    # Показуємо що ввів користувач
    print("Ви ввели:", word)

    # Перевірка регістру
    case_result = check_string_case(word)
    print(case_result)

    # Список літер у верхньому регістрі
    upper_letters = to_uppercase_list(word)
    print("Літери у верхньому регістрі:", upper_letters)

    # Запускаємо генератор і виводимо кілька разів (тут — 8 разів)
    gen = even_odd_generator()
    for _ in range(8):
        print(next(gen))

if __name__ == "__main__":
    main()
