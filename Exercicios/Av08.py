def troca_occ_lista (lst, a, b):
    if len(lst) == 0:
        return lst
    elif lst[0] == a:
        return [b] + troca_occ_lista(lst[1:], a, b)
    return [lst[0]] + troca_occ_lista(lst[1:], a, b)