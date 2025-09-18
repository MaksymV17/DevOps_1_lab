from feature.functions import check_string_case
from feature.generator import even_odd_generator

if __name__ == "__main__":
    # Примеры работы функций
    print(check_string_case("HELLO"))   # Усі літери великі
    print(check_string_case("hello"))   # Усі літери малі
    print(check_string_case("Hello"))   # Змішаний регістр
    print(check_string_case(123))       # Помилка: очікувався рядок

    # Примеры работы генератора
    gen = even_odd_generator()
    for _ in range(5):
        print(next(gen))
