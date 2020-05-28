# Resumo Acelera Dev - Python

## Autor: Pablo Nunes

----

## Veremos nesse módulo

- Funções e Classes
- Herança
- Composição
- Polimorfismo
- Método de Classe
- Método de Instância
- Método Estático

**Extras**:

- Encapsulamento
- Classes abstratas

## Herança

- **Resumo**: De classes genéricas podemos herdar características para fazer classes mais robustas e especialistas.
- Um exemplo:
  - De uma classe Ave pode herdar de uma classe Animal para parte de suas caracteristicas.
  - De uma classe Arara pode herdar de uma classe Ave para parte de suas caracteristicas.
- Cada classe pode extender da maneira que for preciso para adaptar.
- Como exemplo:

```python
class Animal:
    def respirar(self):
        print("Realizando trocas gasosas")


class Mamifero(Animal): # Herdando da classe animal o metodo respirar
    def pelos(self):
        return True


class Cachorro(Mamifero): # Ele herda das duas classes anteriores a ele os metodos Pelos e Respirar.
    def enterrar_osso(self):
        print("O osso foi enterrado")


cao = Cachorro()
cao.respirar()
```

- Isso imprime na tela a definição respirar, mostrando que ele herdou os métodos com sucesso.

- Em Python, podemos fazer Herança multipla. Ou seja, fazer uma classe herdar mais que uma classe. Exemplo:

```python
class Animal:
    def respirar(self):
        print("Realizando trocas gasosas")


class Mamifero(Animal):  # Herdando da classe animal o metodo respirar
    def pelos(self):
        return True


class Domestico():  # Classe nova
    def faz_truques(self):
        print("Fazendo truque")


class Cachorro(Mamifero, Domestico):  # Ele herda das duas classes anteriores a ele os metodos Pelos e Respirar e também a nova classe Domestico.
    def enterrar_osso(self):
        print("O osso foi enterrado")


cao = Cachorro()
cao.respirar()
cao.faz_truques()
```

## Composição

- **Resumo**: Para uma classe específica existir, ela precisa de várias classes para compor esta classe, na qual tem uma associação somente por esta.
- Em python:

```python
# Vamos criar duas classes que vão ser usadas na nossa classe para composição.

class Cliente:  # Classe cliente
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento


class Produto:  # Classe Produto
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


# Vamos criar a classe do carrinho de compras, que vai ter tanto um cliente e varios produtos dentro deste.


class CarrinhoDeCompras:  
    # Note que essa classe não herda nenhuma classe
    # Pois ela só usa os métodos e propriedades mas não é uma forma do mesmo.
    def __init__(self, cliente, produtos):
        self.num_pedido = '1'
        self.produtos = produtos
        self.cliente = cliente

    @property
    # Usando o Property para usar um metodo como uma propriedade
    def valor_carrinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco
        return total

    def adicionar_produto(self, produto);
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def fechar_carrinho(self):
        print(f'Nome do cliente: {self.cliente.nome}')
        print(f'Fechando o pedido: {self.num_pedido}')
        print(f'Valor do carrinho: {self.valor_carrinho}')
```

## Polimorfismo

- **Resumo**: É a capacidade de, em uma classe mais abstrata, definir um comportamento mais genérico, e em suas classes que a herdam, colocamos comportamentos mais especificos.
- Ou seja, fazemos uma classe generica com um espaço vazio e quando vamos fazendo outras, baseadas nela, mais espeificas, colocamos as coisas únicas nestas novas classes.
- Em Python:

```python
class Mamifero:
    def emitir_som(self):
        pass


class Cachorro(Mamifero):  # Estendendo Mamifero
    def emitir_som(self):
        print("au au")


class Gato(Mamifero):  # Estendendo Mamifero
    def emitir_som(self):
        print("Miau Miau")
```

## Método de Classe

- Resumo: Permite você utilizar um método de uma classe, sem precisar fazer uma instância. Pois os metodos são ligados a classe!
- Ela pode ser chamada também do Objeto!
- Lembrando, que se tiver estiver no escopo da instância ```self```, ele não vai poder ser chamado no método, pois está acessível para a classe, que usa ```cls```.
- Em Python:

```python
class Impressora:

    def __init__(self):
        self.a = 10

    @classmethod
    def imprimir_folha(cls):  # Deve funcionar
        print("folha impressa")

    @classmethod
    def imprimir_a(cls):  # Deve dar erro
        print(cls.a)


Impressora.imprimir_folha()  # Mostra na tela o print

impressora = Impressora()  # Fazendo uma instancia

# Os dois comandos devem dar erro
# Impressora.imprimir_a()
# impressora.imprimir_a()

# Eles dão erro pois não tem acesso a instância da variável.
```

## Método de Instância

- Resumo: Nos métodos de instância, eles podem acessar váriaveis em instância da classe e herdam as propriedades dos métodos de classe.
- Assim, eles usam o ```self``` para acessar as variáveis de instância.
- Em python:

```python
class Impressora:

    def __init__(self, numero_folhas):  # Usando o self para construir a função
        self.numero_folhas = numero_folhas

    def imprimir_folha(self):
        print("folha impressa")

    def imprimir_livro(self, paginas):  # Chamando os metodos e variáveis internas
        if paginas <= self.numero_folhas:
            for i in range(paginas):
                self.imprimir_folha()
                self.numero_folhas -= 1

    @classmethod  # Exemplo de método de classe
    def print_modelo(cls):
        print(cls.modelo)


    def print_modelo_instancia(self):
        print(self.modelo)
```

## Método Estático

- Resumo: Ele não usa o escopo da classe, somente o próprio escopo. Ele normalmente é fixo.
- Consigo invocar esse tipo de método em class methods e instâncias.
- Normalmente, usados para tipos de classe factory.
  
````python
class Impressora:
    @staticmethod
    def ligar_para_suporte():
        print("Liguei para o suporte")

    @classmethod
    def deu_problema_na_impressora(cls):
        print("analisando problema")
        cls.ligar_para_suporte()

    def imprimir(self):
        print("imprimindo pagina 1")
        self.ligar_para_suporte()
````

----

## **Extras**

## Encapsulamento

- Resumo: Podemos restringir acesso a métodos e variáveis utilizando ```_``` ou ```__```
- Nesse caso, só poderemos mudar as variáveis usando um setter
- Em Python:
  
````python
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
````

- Ele muda o preço máximo e imprime isso na tela

### [Fonte](https://www.programiz.com/python-programming/object-oriented-programming)

## Classes abstratas

- Resumo: Classes abstratas são classes nas quais não podem ser instanciadas diretamente, além de suas derivadas não poderem usar seus métodos, sendo forçada a implementação de seus métodos.
- Python não vem com as classes abstratas, mas podemos usar uma biblioteca chamada ABC.
- Um método abstrato pode sim ter uma implementação, mas ainda sim precisará de uma sobrecarga.
- Em Python:

````python
from abc import ABC, abstractmethod

class AbsClassExemplo(ABC):  # Herdando da classe ABC, para criar uma classe abstrata

    def __init__(self, value):
        self.value = value

    @abstractmethod  # Força a implementação desse método em classes que a herdam
    def faca_algo(self):
        pass

    @abstractmethod  # Mesmo tendo implementação, ele força colocar algo
    def tem_algo(self):
        print("Há algo aqui?")


class Adiciona1(AbsClassExemplo):  # Fazendo uma classe para dar um Override

    def faca_algo(self):
        return self.value + 1

    def tem_algo(self):
        pass


class TemMais(AbsClassExemplo):

    def faca_algo(self):
        pass

    def tem_algo(self):
        super().tem_algo()
        print("Realmente, tem algo")
````

### [Fonte](https://www.python-course.eu/python3_abstract_classes.php)
