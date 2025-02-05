def filter_by_state(values: list, state: str = "EXECUTED" ) -> list:
    filtered_values = []
    for i in values:
        if i.get("state") == state:
            filtered_values.append(i)
    return filtered_values

def sort_by_date(values: list, setting: bool = True) -> list:
    sorted_values = sorted(values, key=lambda value: value["date"], reverse=setting)
    return sorted_values


