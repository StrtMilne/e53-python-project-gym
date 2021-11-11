def most_common(list):
    result = []
    instances = 0
    
    for item in list:
        occurs = list.count(item)
        if occurs == instances:
            result.append(item)
        if occurs > instances:
            result = []
            result.append(item)
    
    return result