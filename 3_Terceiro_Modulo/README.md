# Resumo Acelera Dev - Python

## Autor: Pablo Nunes

----

## Veremos nesse módulo

- Testes com Python
- Tipos de teste
- TDD
- Pytest

## Topicos Extras
  
- Organização

## Tipos de Teste

- Os testes podem ser classificados como:
  - Teste de Sistema - Testa o sistema como um todo
  - Teste de Integração - Testa uma integração entre dois componentes do sistema
  - Teste Unitário - Testa a menor unidade do sistema
- Os testes tem custo e tempo de execução diferentes

![Pirâmide de testes](./imagens/1.png)

## TDD

- TDD: Desenvolvimento Orientado a Testes
- Vantagens:
  - É uma maneira de desenvolver pensando em testes
  - Guia de design da aplicação
  - Ajuda a entender o problema melhor
  - Garante boa qualidade na aplicação dando segurança em alterações

- Ciclo de desenvolvimento com TDD:
  1. Escreva um teste
  2. Implementa o mínimo para o teste passar
  3. Refatorar o código
  4. Repita

- Instalando o PyTest:

    ```pip install pytest```

- Para o pytest detectar que é um test, no inicio de uma função, é preciso utilizar um *test_* .

- Utilizando o decorator do Pytest com 
  ```@pytest.mark.parametrize('entrada_no_teste', [lista_para_test])```.
  
  É possivel testar várias coisas sem precisar repetir a função!
