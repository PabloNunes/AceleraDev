# Resumo Acelera Dev - Python

## Autor: Pablo Nunes

----

## Veremos nesse módulo

- Variáveis Primitivas e Built-In
- Estruturas de Decisão e Repetição
- Formatação de Strings e pep8

## Variáveis Primitivas e Built-In

- Tipos básicos
  - Em Python, as variáveis primitivas são:
  
  ````python
  nome = 'Pablo N' # String
  idade = 20 # Int
  altura = 1.81 # Float
  tutor = False # Booleano
  trabalhando = None # Não possui valor
  ````

  - É possível fazer operações com as variáveis. Como exemplo:

   ````python
   nova_idade = idade + 30 # Somando int com outro int
   altura_sem_tenis = altura - 5.0 # Subtraindo float com float
   nome_cidade = nome + ' São Paulo' # Concatenando uma string com outra string
   ````

  - Você não pode fazer operações com tipos não compativeis.

   ````python
   nova_idade = idade + nome # Vai retornar um erro
   ````

- Built-In
  - Tipo Lista
    - Recebe várias variáveis que podem ser acessadas de acordo com um indice.
    - Em python:

     ````python
     # Como exemplo, inicializando uma lista de convidados vazia
     lista_convidados = []

     # Inicializando uma lista com alguns nomes
     lista_vip = ['Thiago', 'Pinheiro', 'Mariana', 'Wallace']

     ## Devemos notar que no Python há tipos mutáveis ou imutáveis, a lista é mutável. Ou seja, posso colocar ou remover elementos dela.

     # Adicionando convidados
     lista_convidados.append('Luísa')

     # Removendo convidado VIP
     lista_vip.remove('Thiago')

     # Acessando valores individuais
     print(lista_convidados[0])

     # Pegando o ultimo elemento da lista (Se não souber o tamanho da lista)
     print(lista_convidados[-1])

     # É possível colocar tipos diferentes numa lista mas não é recomendado.
     ````

  - Tipo Tupla
    - A tupla é parecida com a lista, mas ela é imutável!
      - Em python:

      ```python
      # Inicializando a tupla, usando um parentese
      tupla = (1, 2, 3)

      nova_tupla = (3, 2, 1)


      # Essa tupla é uma junção das duas tuplas, ou seja, vai imprimir (1,2,3,3,2,1)
      tupla_teste = tupla + nova_tupla

      ```

    - Tipo dicionário
      - Esse tipo, usa esquema de chave e valor. No qual, você entra a chave, te retornando um valor.
      - Em python:

      ````python
      # Criando um dicionário
      dados_pessoais = {'nome': 'Nomesco Memeiro', 'cidade': 'Atafruta'}

      # Recuperando os dados
      print(dados_pessoais['cidade'])

      # Adcionando dados
      dados_pessoais['idade'] = 25

      # Retirando dados
      del dados_pessoais['idade']

      ````

- Estruturas de decisão
  - AAA
