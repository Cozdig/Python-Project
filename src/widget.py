def mask_account_card(number: str) -> str:
    """Функция принимает на вход номер карты и счета и возвращает их маску, номер карты и номер счета замаскирован."""
    card_number = ""
    name_card = ""
    if "Счёт" in number or "Счет" in number:
        if len(number) - 5 < 20:
            return "Error"
        for num in number[5:]:
            if num.isalpha():
                return "Error"
        else:
            score_number = number[5:]
            number_mask = number[0:4] + " " + "**" + score_number[-4:]
            return number_mask
    else:
        for num in range(len(number)):
            if number[num].isalpha() or number[num] == " ":
                name_card += number[num]
            else:
                card_number += number[num]
        if len(card_number) < 16:
            return "Error"
        for num in range(len(card_number)):
            if card_number[num].isalpha():
                return "Error"
        else:

            correct_number = card_number[0:7] + card_number[7:14] + card_number[14:19]
            number_mask = (
                name_card
                + correct_number[0:4]
                + " "
                + correct_number[4:6]
                + "**"
                + " "
                + "****"
                + " "
                + correct_number[12:16]
            )

            return number_mask


def get_date(date: str) -> str:
    """Функция принимает на вход строку и отдает корректный результат в формате 11.07.2018."""
    if len(date) < 26 or len(date) > 26:
        return "Error"
    else:
        correct_date = date[8:10] + "." + date[5:7] + "." + date[0:4]
        return correct_date
