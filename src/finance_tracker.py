import csv
import pandas as pd

def transactions(file):
    """Эта функция читает csv файл и выводит результат в консоль."""
    try:
        with open(file) as csv_f:
            reader = csv.DictReader(csv_f, delimiter=";")
            operations = [row for row in reader]
            return operations
    except Exception:
        return "Файл не найден"

def transactions_excel(file):
    """Эта функция читает xlsx файл и выводит результат в консоль."""
    try:
        with open(file, encoding="utf-8") as xlsx_f:
            df = pd.read_excel(xlsx_f)
            operations = df.to_dict(orient="records")
            return operations
    except Exception:
        return "Файл не найден"
