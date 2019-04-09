class arvore:
    def __init__(self, args):
        if args == ():
            self.r = None
        else:
            if len (args) == 3:
                if isinstance (args[1], arvore) and isinstance(args[2], arvore):
                    sefl.r = args [0]
                    self.e = args [1]
                    self.d = args [2]
                else:
                    raise ValueError ('arvore: ...')
            else:
                raise ValueError ('arvore: ...')
    
    def raiz (self):
        if self.r == None:
            raise ValueError('raiz: a árvore é vazia')
        else:
            return self.r
    
    def arv_esq (self):
        if self.e == None:
            raise ValueError('raiz: a árvore é vazia')
        else:
            return self.e
    
    def arv_dir (self):
        if self.d == None:
            raise ValueError('raiz: a árvore é vazia')
        else:
            return self.d
    
    def muda_raiz(self, r):
        if self.r == None:
            self.e = arvore ()
            self.d = arvore ()
        self.r = r
    
    def muda_arv_esq(self, a_e):
        if self.r == None:
            raise ValueError ('muda_arv_esq:...')
        else:
            self.e = a_e
    
    def muda_arv_dir (self, a_d):
        if self.r == None:
            raise ValueError ('muda_arv_esq:...')
        else:
            self.d = a_d


# Exercicio 1:
def numero_nos_arv (arv):
    if arv_vazia(arv):
        return 0
    else:
        return 1 + numero_nos_arv(arv_esq(arv)) + numero_nos_arv(arv_dir(arv))

# Exercício 2:
def prof_max_arv (arv):
    if arv_vazia(arv):
        return -1
    else:
        return 1 + max(prof_max_arv (arv_esq (arv)), prof_max_arv (arv_dir (arv)))

# Exercício 3:
def soma_elementos_arv (arv):
    if arv_vazia (arv):
        return 0
    else:
        return raiz (arv) + soma_els_arv (arv_esq(arv)) + soma_els_arv(arv_dir(arv))