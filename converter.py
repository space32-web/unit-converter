"""Конвертер единиц длины."""

LENGTH_UNITS = {"мм": 0.001, "см": 0.01, "м": 1.0, "км": 1000.0}


def convert_length(value, from_unit, to_unit):
    """Переводит длину из одной единицы в другую."""
    if from_unit not in LENGTH_UNITS or to_unit not in LENGTH_UNITS:
        raise ValueError("Неизвестная единица длины")
    meters = value * LENGTH_UNITS[from_unit]
    return meters / LENGTH_UNITS[to_unit]


def main():
    """Читает запрос вида '5 км м' и выводит результат."""
    try:
        value, from_unit, to_unit = input("Например, '5 км м': ").split()
        result = convert_length(float(value), from_unit, to_unit)
        print(f"{value} {from_unit} = {result:g} {to_unit}")
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
