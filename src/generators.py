def filter_by_currency(transactions, currency):
    """Эта функция принимает на вход список транзакций и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    filtered_transactions = filter(
        lambda transaction: transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency,
        transactions,
    )
    for sort in filtered_transactions:
        yield sort


def transaction_descriptions(transactions):
    """Эта функция принимет на вход список транзакций и выдает описание каждой по очереди."""
    for tran in transactions:
        if tran == {}:
            pass
        else:
            yield tran.get("description")


def card_number_generator(start, last):
    """Эта функция принимает на вход начальное и конечное значение номра карты,
    чтобы сгенерировать несколько номеров карт в зависимости от указанного диапазона."""

    def format_card_number(number):
        """Эта функция выполняет форматирование номера карты, чтобы он соответствовал стандартному формату."""
        string = f"{number:016}"
        return " ".join([string[i : i + 4] for i in range(0, len(string), 4)])

    while start <= last:
        yield format_card_number(start)
        start += 1
