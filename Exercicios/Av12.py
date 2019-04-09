# exemplo: colapsa_arv(lambda x,y: x + y, arv, 0)
def colapsa_arv (f, arv, el_neutro):
    if arv_vazia (arv):
        return el_neutro
    else:
        return f(raiz(arv), f(colapsa_arv(arv_esq(arv)), colapsa_arv(arv_dir(arv))))