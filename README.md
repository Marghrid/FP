# Fundamentos da Programação

**Instituto Superior Técnico - 1º Semestre 2015/16**

Projetos e exercícios de programação da disciplina.

## Projetos

### Proj1: 
Programa em Python que permita distribuir mandatos a deputados na Assembleia da República segundo o método D’Hondt, dado o número de votos numa eleição.

Execução e exemplo de interação:

```console
cd Proj1
python3

```

```console
>>> from proj1 import *
>>> votacoes = ((0, 15729, 220408, 1297, 0, 3040, 993, 0, 1354, 1046, 0, 3284, 99652, 19327, 0), (0, 19000, 23173, 255, 0, 532, 201, 0, 306,\
232, 0, 1980, 22307, 3890, 0), (0, 23731, 244971, 1959, 0, 2710, 1465, 0, 1094, 1114, 0, 4264, 159476, 20488, 0), (0, 1956, 47716, 282, 0, 0,\
175, 0, 165, 247, 0, 417, 19728, 1732, 0), (0, 5384, 52325, 403, 0, 770, 543, 0, 428, 0, 0, 1454, 38317, 4609, 0), (0, 14138, 113419, 662,\
0, 2535, 600, 0, 591, 557, 0, 2014, 66199, 13034, 0), (0, 18967, 31260, 237, 0, 649, 216, 0, 168, 207, 0, 1810, 25010, 4225, 0), (0,\
17255, 99745, 2076, 0, 3285, 0, 0, 1069, 700, 0, 3160, 46082, 16347, 0), (0, 3299, 53450, 251, 0, 520, 199, 0, 178, 191, 0, 755, 26263,\
3114, 0), (0, 12351, 148762, 977, 0, 3029, 633, 0, 595, 453, 0, 2502, 51518, 0, 0), (0, 111661, 560365, 4135, 0, 16913, 2410, 0, 5897, 4270,\
0, 14419, 322034, 66874, 0), (0, 7910, 26257, 176, 0, 333, 162, 0, 151, 135, 0, 1031, 19963, 2753, 0), (0, 61832, 488402, 2413, 0, 9072,\
3386, 0, 1551, 1525, 0, 9640, 318113, 51002, 0), (0, 21347, 118028, 1454, 0, 2220, 692, 0, 832, 726, 0, 3413, 61194, 13712, 0), (0, 82159,\
156444, 1682, 0, 6282, 1133, 0, 1595, 847, 0, 0, 112764, 29667, 0), (0, 6648, 76961, 384, 0, 926, 0, 0, 213, 331, 0, 1473, 35327, 5928,\
0), (0, 3656, 71840, 304, 0, 617, 254, 0, 147, 574, 0, 675, 34825, 2784, 0), (0, 5810, 123184, 696, 0, 1229, 465, 0, 266, 626, 0, 1456,\
54107, 5786, 0), (0, 2288, 53518, 314, 0, 756, 293, 0, 219, 271, 0, 669, 23189, 3965, 0), (0, 5096, 87597, 2560, 0, 2385, 2992, 0, 617,\
538, 0, 1967, 20360, 5568, 0), (0, 803, 6306, 101, 0, 192, 83, 0, 48, 50, 0, 132, 7205, 602, 0), (0, 127, 8938, 87, 0, 0, 0, 0, 64, 47, 0,\
52, 2714, 165, 0))
>>> mandatos(19, votacoes[2])
(0, 1, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0)
>>> mandatos(3, votacoes[3])
(0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0)
>>> assembleia(votacoes)
(0, 16, 137, 0, 0, 0, 0, 0, 0, 0, 0, 0, 71, 6, 0)
>>> max_mandatos(votacoes)
’PPD/PSD-CDS/PP\tPortugal a Frente’
>>>
```

Autores:
- [Margarida Ferreira](https://github.com/Marghrid)
- [Miguel Marques](https://github.com/miguelmarques1904)

Outubro 2015

### Proj2:
Programa em Python que permite a um utilizador jogar o _Picross_.

Execução e exemplo de interação:

```console
cd Proj2
python3

```
```console
>>> from proj2 import * 
>>> jogo_picross('jogo_fig2.txt')
JOGO PICROSS
       1                   
  2    2    2    3    3    
[ ? ][ ? ][ ? ][ ? ][ ? ] 2  |
[ ? ][ ? ][ ? ][ ? ][ ? ] 3  |
[ ? ][ ? ][ ? ][ ? ][ ? ] 2  |
[ ? ][ ? ][ ? ][ ? ][ ? ] 2 2|
[ ? ][ ? ][ ? ][ ? ][ ? ] 2  |

Introduza a jogada
- coordenada entre (1 : 1) e (5 : 5) >> (4 : 1)
- valor >> 2
       1                   
  2    2    2    3    3    
[ ? ][ ? ][ ? ][ ? ][ ? ] 2  |
[ ? ][ ? ][ ? ][ ? ][ ? ] 3  |
[ ? ][ ? ][ ? ][ ? ][ ? ] 2  |
[ x ][ ? ][ ? ][ ? ][ ? ] 2 2|
[ ? ][ ? ][ ? ][ ? ][ ? ] 2  |

Introduza a jogada
- coordenada entre (1 : 1) e (5 : 5) >> (4 : 2)
- valor >> 2
       1                   
  2    2    2    3    3    
[ ? ][ ? ][ ? ][ ? ][ ? ] 2  |
[ ? ][ ? ][ ? ][ ? ][ ? ] 3  |
[ ? ][ ? ][ ? ][ ? ][ ? ] 2  |
[ x ][ x ][ ? ][ ? ][ ? ] 2 2|
[ ? ][ ? ][ ? ][ ? ][ ? ] 2  |

Introduza a jogada
- coordenada entre (1 : 1) e (5 : 5) >> 

[...]
```

Autores:
- [Margarida Ferreira](https://github.com/Marghrid)
- [Miguel Marques](https://github.com/miguelmarques1904)

Dezembro 2015

## Exercícios:

__a02__: Elementos básicos de programação

__a03__: Funções

__a04__: Tuplos e ciclos contados

__a05__: Listas

__a06__: Funções recursivas e funções de ordem superior

__a07__: Recursão e iteração

__a08__: Dicionários

__a09__: Abstração de Dados

__a10__: Ficheiros

__a11__: Programação com objetos

__a12__: Estruturas Lineares
