def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    # TODO: Фейлятся тесты на невалидность, но при это работают тесты на корректность. Надо как-то проверить
    # TODO: что первый символ является открывающей скобочкой, а второй - закрывающей.
    valid_start = []
    valid_end = []
    list_of_brackets = list(brackets_row)
    for i in list_of_brackets:
        if i == "(":
            valid_start.append(i)
        elif i == ")":
            valid_end.append(i)
    print(valid_start)
    print(valid_end)
    if len(valid_start) == len(valid_end):
        return True
    else:
        return False


check_brackets('()()()')
check_brackets("")
