def even_odd_generator():
    n = 0
    while True:
        if n % 2 == 0:
            yield "Парне"
        else:
            yield "Непарне"
        n += 1
