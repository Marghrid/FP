def maior_elemento(conjunto):
    
    maximo = conjunto[0]
    
    for i in conjunto:
        if i > maximo:
            maximo = i

    return maximo