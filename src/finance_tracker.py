import csv

import pandas as pd


def transactions(file):
    """Эта функция читает csv файл и выводит результат в консоль."""
    try:
        with open(file, encoding="utf-8") as csv_f:
            reader = csv.DictReader(csv_f, delimiter=";")
            operations = [row for row in reader]
            return operations
    except Exception:
        return "Файл не найден"


def transactions_excel(file):
    """Эта функция читает xlsx файл и выводит результат в консоль."""
    try:
        df = pd.read_excel(file)
        operations = df.to_dict(orient="records")
        return operations
    except FileNotFoundError:
        return "Файл не найден"
    except Exception as e:
        return f"Ошибка: {e}"


print(transactions("..\\data\\transactions.csv"))
print(transactions_excel("..\\data\\transactions_excel.xlsx"))
