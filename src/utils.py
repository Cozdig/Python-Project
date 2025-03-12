import json


def json_transactions(way):
    """Функция принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых транзакциях."""
    try:
        with open(way, encoding="utf-8") as f:
            data = json.load(f)
            if data == "" or type(data) != list:
                return []
            else:
                return data
    except Exception:
        return []
