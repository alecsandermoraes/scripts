# Variável 
var = ''

# Tipos de Dados 
integer = 10                                    # int 
decimal = 3.14                                  # float
string = 'Hello, World!'                        # str 
boolean = True                                  # bool 
lis = [1, 2, 3]                                 # list 
tup = ('Rosa', 'Vermelho')                      # tuple 
dic = {'Nome': 'Laura', 'Idade': 16}            # dict 
s = {26, 10, 3, 2}                              # set
im_set = frozenset({1, 2, 3})                   # frozenset 
data = bytes([65, 66, 67])                      # bytes 
b_arr = bytearray([65, 66, 67])                 # bytearray 
buffer = memoryview(b'Example')                 # memoryview 

# Operadores 

## Aritméticos 
10 + 2      # Soma - 12 
10 - 2      # Subtração - 8 
10 * 2      # Multiplicação - 20 
10 / 2      # Divisão - 5.0 
10 // 2     # Divisão Exata - 5 
10 % 2      # Resto da Divisão - 0  
10 ** 2     # Potenciação - 100 

# Lógicos 

## AND
True and True       # True 
True and False      # False
False and True      # False 
False and False     # False 

## OR
True or True        # True 
True or False       # True 
False or True       # True 
False or False      # False 

## NOT 
not True    # False 
not False   # True 

# Associação 
a = str()
b = list() 

a in b          # A está em B 
a not in b      # A não está em B 

# Identidade 
a = True 

a is bool       # A é booleano
a is not bool   # A não é booleano 

# Relacionais 
a = 5 
b = 2 

a == b      # Igual a - False   
a != b      # Diferente de - True 
a > b       # Maior que - True 
a < b       # Menor que - False 
a >= b      # Maior ou Igual que - True 
a <= b      # Menor ou Igual que - False 

# Atribuição 
a = 5       # Atribuição - 2 
a += 2      # Atribuição de Soma - 7 
a -= 2      # Atribuição de Subtração - 3 
a *= 2      # Atribuição de Multiplicação - 10 
a /= 2      # Atribuição de Divisão - 2.5 
a //= 2     # Atribuição de Divisão Exata - 2 
a %= 2      # Atribuição de Resto da Divisão - 1 
a **= 2     # Atribuição de Potenciação - 25 

# Condicionais
idade = 10 

if idade >= 18:
    # Condicional Simples
    print('Maior de Idade')

if idade >= 18:
    print('Maior de Idade')
else:
    # Condicional Composta
    print('Menor de Idade')

if idade >= 18:
    print('Maior de Idade')
elif idade >= 65:
    # Condicional Aninhada
    print('Idoso(a)')
else:
    print('Menor de Idade')

# Estruturas de Repetição 
indice = 0 

while indice < 5:
    # While 
    print(indice)
    indice += 1 

lista = [0, 1, 2, 3]
while indice < len(lista):
    # While-In 
    print(lista[indice])
    indice += 1

for i in range(5):
    # For (range)
    print(i)

frutas = ['Maçã', 'Banana', 'Laranja']
for fruta in frutas:
    # For (iterable)
    print(fruta)

# Tratamento de Erros e Exceções 
try:
    # Código que será executado 
    resultado = 5 / 0 
except ZeroDivisionError:
    # Código para uma exceção 
    print('Erro: Tentativa de Divisão por Zero')
else:
    # Código caso nenhuma exceção seja levantada 
    print('Deu Tudo Certo') 
finally:
    # Código do fim do programa, com ou sem exceção 
    print('Fim do Programa')

# Importações
from math import pi 
from math import * 
import math as m 
import math 
