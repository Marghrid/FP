def parte(lst, el):
    result = [[],[]]
    for num in lst:
        if num < el:
            result[0] = result[0] + [num]
        else:
            result[1] = result[1] + [num]

    return result