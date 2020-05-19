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
  - Como podemos usar variáveis para tomar decisões de acordo com nosso código.
  - If:
    - Usando uma condição para avaliar, assim podemos ter um verdadeiro ou falso que vai passar para o bloco de código ou não.
    - Podemos observar no Python:

    ````python
    # Incializando a váriavel para usar no if
    idade = 19

    # Colocando o if e o else.
    # O if é caso a váriavel satisfaça a condição, ela vai continuar no bloco.
    # O else é o caso que a váriavel não satisfaça a condição do if, e prossegue no bloco de código no else.

    if idade < 18:
      print("Pessoa menor de idade")
    else:
      print("Pessoa maior de idade")
    ````

    - As condições do if podem ser satisfeitas com os diversos tipos do python e concatenadas.
    - Em Python:

    ````python
    # Fazendo um dicionário
    veiculo = {'tipo': 'carro', 'marca': 'Fiat', 'potencia_motor': 140}

    # Usando a condição

    if veiculo['tipo'] == 'moto' and veiculo['marca'] == 'Honda':
      print("Esse veículo é uma moto Honda")
    else:
      print("O veículo não é uma moto Honda")


    ## Podemos notar que esse comando usa um tipo booleano para controlar o fluxo do código

    booleano_demo = (veiculo['tipo'] == 'moto' and veiculo['marca'] == 'Honda') # Aloca um booleano aqui

    ## Assim, podemos utilizar lógica para fazer nossas sentenças. Como exemplo:

    if veiculo['tipo'] == 'moto' or veiculo['potencia_motor'] > 120:
      print('Você tem um veículo rápido')
    else:
      print("Você tem um veículo lento :(")

    # Sentença lógica maior, utilizando priorização.

    if (veiculo['tipo'] == 'moto' or veiculo['potencia_motor'] > 120) or veiculo['marca'] == 'Ferrari' :
      print('Veículo muito bom')
    else:
      print(":(")
    ````

    - Você também pode usar o ``elif``, que é um if só que concatenado com o primeiro if.
    - Como exemplo:

    ````python
    if veiculo['tipo'] == 'moto':
      print("É uma moto")
    elif veiculo['tipo'] == 'carro': # Uso do elif depois de um if, para continuar checando
      print("É um carro")
    else:
      print("Não sei que é!")
    ````

    - Strings, listas, dicionários podem ser checadas se estão preenchidas ou não por um if, se tiverem vazias elas são consideradas como falsas, exemplo:

    ````python
    string_nome = 'Algo'

    if string_nome:
      print("Há algo") # Vai sair essa opção
    else:
      print("Não há nada")

    ## Agora não vai ter nada na string

    string_none = ''

    if string_none:
      print("Há algo")
    else:
      print("Não há nada") # Vai sair essa opção

    ## Em listas, você precisa usar a função len para poder usar nesse contexto. (E dicionários!)

    lista_teste = [1,2,3]

    if len(lista_teste):
      print("Há algo") # Vai sair essa opção
    else:
      print("Não há nada")
    ````

- Estruturas de Repetição
  - For
    - O for do Python funciona de diversas maneiras, primeiramente vamos usar um contador para mostrar.
    - Em python:

    ````python
    for i in range(10): # Esse range ele muda o i, para variar entre 0 a 9.
      print(i) # Vai imprimir numeros de 0 a 9
    ````

    - For pode também iterar sobre listas, como exemplo pegando cada item da lista.
    - No python:

    ````python
    convidados = ['Alessandro', 'Bruno', 'Caio', 'Daniel', 'Felix']

    for convidado in convidados: # Ele vai pegar cada membro da lista e colocar em convidado
      print(convidado)

    # Suponha que você quer iterar a lista pela contagem, você pode
    for i in range(len(convidados)):
      print(convidado[i] + ' foi convidado!')
    ````

  - While
    - Agora, vamos supor que sua repetição tem uma condição para acabar. Neste caso, você pode usar um ``while``, no qual vai parar de fazer a repetição quando se cumprir.
    - Em python:

    ````python
    loop_while = True # Começando com um booleano
    contador = 0

    while loop_while:
      contador += 1

      if contador == 5: # Sem essas condições ele fica loopando infinito!
        loop_while = False

      print('Contador ' + str(contador))

    # Reorganizando a função
    contador = 0

    while contador < 5:
      contador += 1 # Agora, ele está limitado pela condição lógica acima, assim podemos tirar a troca do booleano
      print('Contador ' + str(contador))
    ````

- Strings
  - Nas strings precisamos tomar cuidado com a formatação!
  - Python:

  ````python
  # Podemos colocar um int na string de duas formas

  idade = 19

  # Primeira, usando um cast para o int
  print('Minha idade é ' + str(idade))

  # Segunda, usando o format
  print('Minha idade é {}'.format(idade))

  # Terceira, usando as fstrings
  print(f'Minha idade é {idade}')
  ````

  - A ````fstring```` permite formatações especiais e mais flexibilidade para manipular as strings.
  - Como exemplo:
  
  ````python
  # A fstring permite formatações especiais
  nome = 'Roberto'
  idade = 19

  print(f'Meu nome é {nome} e eu tenho {idade} anos')

  # Vamos limitar o tamanho do nome
  Nome = 'Paralelepípedo Souza Costa Moreira'

  print(f'Meu nome é {nome:.10} e eu tenho {idade:03} anos') # Usando o :.10 ele limitou o nome em 10 characteres! Forçou também a idade ter 3 catacteres!

  # Um bom caso para os fstrings são mostrando formatos mais complexos.

  total_compra = 7.5

  print(f'O total da compra deu {total_compra:.2f} reais!') # Esse .2f, mostra que ele está forçando o ponto flutuante a mostrar duas casas decimais. Ficando mais legivel para o consumidor. Ele também arredonda.

  #fstring acessa tudo diretamente inclusive indices de listas

  jantar_restaurante = ['arroz', 'baião', 'bife', 'ovo poché', 'batata frita', 'maminha']

  print(f'Comi no restaurante {jantar_restaurante[1]}, {jantar_restaurante[-1]} e {jantar_restaurante[4]}!') # Acessando a lista, ele comeu baião, maminha e batata frita!

  # Posso, fazer operações dentro da fstring!

  print(f'Eu terei {idade + 5} daqui a cinco anos!!')
  ````

- Formatação pep8
  - O que é o pep8?
    - Define uma formatação de código para o Python, sugerido pela comunidade.
  - Para nos ajudar, podemos instalar uma lint para verificar nosso código e mostrar pontos que podem ser melhorados.
  - No pep8, vamos utilizar o flake8, usando o pip.
  - > ```pip install flake8```
  - No terminal, usando:
  - > ```flake8 codigo.py```
  - Ele vai retornar onde podemos mudar nosso código!
