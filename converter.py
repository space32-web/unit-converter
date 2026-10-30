"""Конвертер единиц длины и температуры."""

LENGTH_UNITS = {"мм": 0.001, "см": 0.01, "м": 1.0, "км": 1000.0}
TEMPERATURE_UNITS = ("C", "F", "K")


def convert_length(value, from_unit, to_unit):
    """Переводит длину из одной единицы в другую."""
    if from_unit not in LENGTH_UNITS or to_unit not in LENGTH_UNITS:
        raise ValueError("Неизвестная единица длины")
    meters = value * LENGTH_UNITS[from_unit]
    return meters / LENGTH_UNITS[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """Переводит температуру между шкалами Цельсия, Фаренгейта и Кельвина."""
    if from_unit not in TEMPERATURE_UNITS or to_unit not in TEMPERATURE_UNITS:
        raise ValueError("Неизвестная шкала температуры")
    celsius = {
        "C": value,
        "F": (value - 32) * 5 / 9,
        "K": value - 273.15,
    }[from_unit]
    return {
        "C": celsius,
        "F": celsius * 9 / 5 + 32,
        "K": celsius + 273.15,
    }[to_unit]


def convert(value, from_unit, to_unit):
    """Выбирает нужный конвертер по единицам измерения."""
    if from_unit in TEMPERATURE_UNITS:
        return convert_temperature(value, from_unit, to_unit)
    return convert_length(value, from_unit, to_unit)


def main():
    """Читает запрос вида '5 км м' или '100 C F' и выводит результат."""
    try:
        value, from_unit, to_unit = input("Например, '5 км м': ").split()
        result = convert(float(value), from_unit, to_unit)
        print(f"{value} {from_unit} = {result:g} {to_unit}")
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
