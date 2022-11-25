def is_anagram(first_string: str, second_string: str) -> tuple:
    sortedFirst = sortString(first_string.lower())
    sortedSecond = sortString(second_string.lower())
    print(sortedFirst, sortedSecond, sortedSecond == sortedFirst)
    return (sortedFirst, sortedSecond, sortedSecond == sortedFirst)


def sortString(valueString: str) -> str:
    sort = list(valueString)
    sortUpdated = list(valueString)
    for index in valueString:
        for i in range(len(valueString) - 1, 0, -1):
            if sortUpdated[i] < sortUpdated[i - 1]:
                sort[i] = sortUpdated[i - 1]
                sort[i - 1] = sortUpdated[i]
                sortUpdated = sort.copy()
    return "".join(sort)
