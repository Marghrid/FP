def soma_els_atomicos (lst):
    if len(lst) == 0:
        return 0
    elif not isinstance(lst[0], list): 
        return lst[0] + soma_els_atomicos(lst[1:])
    else:
        return soma_els_atomicos(lst[0]) + soma_els_atomicos(lst[1:])



def soma_els_atomicos2 (lst):
    if not lst:
        return 0
    if not isinstance(lst[0], list): 
        return lst[0] + soma_els_atomicos(lst[1:])
    return soma_els_atomicos(lst[0]) + soma_els_atomicos(lst[1:])