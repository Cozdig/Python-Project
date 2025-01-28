def get_mask_card_number() -> str:
    """Функция принимает на вход номер карты и возвращает ее маску, номер карты замаскирован."""
    number = input("Ваш номер карты:")
    card_number = ""
    for i in range(len(number)):
        if number[i].isalpha() or number[i] == " ":
            pass
        else:
            card_number += number[i]

    correct_number = card_number[0:7] + card_number[7:14] + card_number[14:19]
    number_mask = correct_number[0:4] + " " + correct_number[4:6] + "**" + " " + "****" + " " + correct_number[12:16]
    return number_mask


def get_mask_account() -> str:
    """Функция принимает на вход номер счета и возвращает его маску, номер счета замаскирован."""
    number = input("Ваш номер счета:")
    number_mask = "**" + number[-4:]
    return number_mask


def get_date() -> str:
    """Функция принимает на вход строку и отдает корректный результат в формате 11.07.2018."""
    date = input("Введите дату:")
    correct_date = date[0:2] + "." + date[2:4] + "." + date[4:]
    return correct_date


print(get_date())
