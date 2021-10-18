from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(cls, iterable):
        cls.iterable = iterable
        cls.position = 0

    def __next__(cls):
        try:
            valor_atual = cls.iterable[cls.position]
        except IndexError:
            raise StopIteration()
        else:
            cls.position += 1
            return valor_atual
