
# -=-=- Continuação: Tipos Estruturados -=-=-

# Métodos que resultam em valores booleanos:

string = 'abcd1234'

print(string.isalnum()) # <- Retorna True se é alfanumérico (com letras de a-z A-Z e numeros 0-9).

print(string.isalpha()) # < Retorna True se os caracteres alfabéticos (a-z A-Z).

print(string.isupper()) # < Retorna True se os caracteres estão em caixa alta.

print(string.islower()) # < Retorna True se os caracteres estão em caixa baixa.

print(string.isnumeric()) # < Retorna True se os caracteres são númericos(0-9).
print(string.isdigit()) # < Retorna True se os caracteres são númericos(0-9)(RECOMENDADO).
print(string.isdecimal()) # < Retorna True se os caracteres são númericos(0-9).

string = 'abcdefjgh'

print(string.startswith('abc')) # < Retorna True se a string começar com o valor informado (no caso 'abc').
print(string.startswith('abc', 3, 5)) # < Retorna True se a string começar com o valor informado (no caso 'abc') a partir do valor fatiado.

print(string.endswith('jgh')) # < Retorna True se a string terminar com o valor informado (no caso 'jgh').
print(string.endswith('jgh', 3, 5)) # < Retorna True se a string terminar com o valor informado (no caso 'jgh') a partir do valor fatiado.

print(string.casefold() == 'abcdefjgh') # < Retorna True se forem igual as comparações transformando a string em caixa baixa.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Formatações para string:

string = 'abcdefjgh'

print(string.upper()) # <- Transforma a string em caixa alta.

print(string.lower()) # <- Transforma a string em caixa baixa.

print(string.lower()) # <- Transforma a string em caixa baixa.

string = 'abcdEFGH'

print(string.swapcase()) # <- Troca todos os caracteres em caixa baixa e transforma-os em caixa alta e vice-versa.

string = 'hoje está vento amigao'

print(string.title()) # <- Transforma cada letra de cada palavra em caixa alta e as demais em minúsculo.
                      # Funciona com qualquer caractere que não seja letra separando as palavras(' ', '&', '*'...)

print(string.count('o')) # <- Conta a quantidade de ocorrencias de alguma coisa.

print(string.find('j')) # <- Informa o índice da PRIMEIRA ocorrencia de alguma coisa.
print(string.rfind('o')) # <- Informa o índice da ÚLTIMA ocorrencia de alguma coisa.

print(string.index('j')) # <- Informa o índice da PRIMERA ocorrencia de alguma coisa (com a diferença que se ela não existir dá erro).
print(string.rindex('o')) # <- Informa o índice da PRIMERA ocorrencia de alguma coisa.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Edição e substituição de string:

print(string.center(50))  # <- Centraliza a string em x caracteres.
print(string.center(50, '.'))  # <- Centraliza a string em x caracteres com o caractere que quiser na esquerda e direita.

string = 'hoje\testá\tvento\tamigao'
print(string.expandtabs(25))  # <- Transforma a tabulação com a quantidade de espaço que for informado.

string = 'hoje está vento amigao'

print(string.strip(' ')) # <- Retira caracteres com o valor informado do inicio e do fim.
print(string.rstrip('-')) # <- Retira caracteres com o valor informado do fim (da direita).
print(string.lstrip('*')) # <- Retira  caracteres com o valor informado do início (da esquerda).

string = 'David'

print(string.rjust(10)) # <- Justifica a string com x espaços em bracos a direita.
print(string.rjust(10, '-')) # <- Justifica a string com x caracteres informados a direita.

print(string.ljust(10)) # <- Justifica a string com x espaços em bracos a esquerda.
print(string.ljust(10, '<')) # <- Justifica a string com x caracteres informados a esquerda.

print(string.replace('a', 'x')) # <- Substitui todas as ocorrencias de 'x' por 'y'.


string = 'hoje está vento amigao'
de  = 'oale' # <- Tabela de tradução
para = '0413' # <- Idem
tabela = str.maketrans(de, para)
print(string.translate(tabela)) # <- Troca todos pela tabela.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Agrupa e separa strings:

string = ['hoje', 'está', 'vento', 'amigao']
print(' '.join(string)) # <- Junta a todos os elementos lista acima separado pelo primeiro caractere informado.

string = 'hoje está vento amigao'

print(string.split(' ')) # <- Separa a string por o caractere informado, transformando-a em uma lista.
print(string.split(' ', maxsplit=3)) # <- Separa a string por o caractere informado, transformando-a em uma lista com seu limite informado.
print(string.rsplit(' ', maxsplit=3)) # <- Separa a string pelo final por o caractere informado, transformando-a em uma lista com seu limite informado.

print(string.splitlines()) # <- Quebra a string por linha transformando-a em uma lista

print(string.partition(' ')) # <- Quebra a string pelo caractere informado, transformando-a em uma tupla.
print(string.rpartition(' ')) # <- Quebra a string pelo final pelo caractere informado, transformando-a em uma tupla.
