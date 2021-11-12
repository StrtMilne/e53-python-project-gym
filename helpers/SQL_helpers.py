def most_common(list):
    result = []
    tried = []
    instances = 0

    for item in list:
        occurances = list.count(item)
        if item not in tried:
            if occurances == instances:
                result.append(item)
            if occurances > instances:
                instances = occurances
                result = []
                result.append(item)
        tried.append(item)

    return result