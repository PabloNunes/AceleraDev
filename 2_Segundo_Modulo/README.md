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
